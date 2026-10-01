from django.core.management.base import BaseCommand

from products.models import Product, PriceHistory

from products.scraper import get_price

from products.notifier import send_price_alert


class Command(BaseCommand):

    help = "Check product prices and send alerts"

    def handle(self, *args, **kwargs):

        products = Product.objects.all()

        for product in products:

            price = get_price(product.url)

            if price:

                # Update current price
                product.last_price = price
                product.save()

                # Save price history
                PriceHistory.objects.create(
                    product=product,
                    price=price
                )

                # Check target price
                if price <= product.target_price:

                    send_price_alert(product)

                self.stdout.write(
                    self.style.SUCCESS(
                        f"{product.name} → Current price: {price}"
                    )
                )

            else:

                self.stdout.write(
                    self.style.WARNING(
                        f"Could not fetch price for {product.name}"
                    )
                )