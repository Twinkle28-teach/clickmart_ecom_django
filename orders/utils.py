from django.core.mail import send_mail 
from django.conf import settings


def send_order_notification(order):
    send_mail(
        subject= f"order #{order.id} is received.",
        message= f"""
            Hi {order.user.first_name},

            Your order #{order.id} has been placed,

            Total: {order.grand_total}
            
            Thank you for shipping with us.
            """,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[order.user.email],
            fail_silently= False

    )