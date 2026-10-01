from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    target_price = models.FloatField()
    last_price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="price_history"
    )

    price = models.FloatField()

    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - ₹{self.price}"