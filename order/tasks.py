from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id = order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear, {0}, Thank you for your purchase.' \
              'Your order number is: {1}'.format(order.name, order.id)

    mail = send_mail(subject, message, 'asdf@gmail.com', [order.email])
    return mail