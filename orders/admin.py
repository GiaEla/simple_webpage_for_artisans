from django.contrib import admin

# Register your models here.
from orders.models import Product

admin.site.register(Product)