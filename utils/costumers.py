import datetime

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from orders.models import Order, Product


def create_order(form, product_pk):
    order = Order()
    order.date = datetime.datetime.now()
    order.recipient_email = form.cleaned_data['email']
    order.comment = form.cleaned_data['comment']
    order.product_fk = Product.objects.get(id=product_pk)
    order.status = "Naročilo prejeto"

    order.save()

    return order


def send_email(order):

    subject = 'Naročilo ' + order.product_fk.name
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [order.recipient_email]

    message = render_to_string('order_confirmation.html')
    text_message = strip_tags(message)

    mail = EmailMultiAlternatives(subject, text_message, to=to, from_email=from_email)
    mail.attach_alternative(message, "text/html")

    mail.send()