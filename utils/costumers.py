import datetime

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from orders.models import Order, Product


def create_order(form, product_pk):
    order = Order()
    order.date = datetime.datetime.now()
    order.recipient_email = form.cleaned_data['email']
    order.product_fk = Product.objects.get(id=product_pk)
    order.status = "Naročilo prejeto"

    order.save()

    return order


def send_email(order):

    subject = 'Naročilo izdelka ' + order.product_fk.name
    message = render_to_string('order_confirmation.html')
    recipient_email = order.recipient_email

    email = EmailMessage(
        subject,
        message,
        'giacotesting@gmail.com',
        [recipient_email],
    )

    email.content_subtype = 'html'
    email.send()