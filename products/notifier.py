from django.core.mail import send_mail
from django.conf import settings


def send_price_alert(product):
    send_mail(
        subject="Price Drop Alert!",
        message=f"{product.name} price dropped to {product.last_price}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
    )
