from django.contrib import admin

# Register your models here.
from orders.models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'size', 'price', 'sold')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_fk', 'recipient_email', 'date', 'status')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)