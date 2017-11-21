from django import forms
from django.contrib import admin

# Register your models here.
from orders.models import Product, Order


class OrderModelForm(forms.ModelForm):
    comment = forms.CharField(label='Opombe', widget=forms.Textarea)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('fotografija', 'name', 'size', 'price', 'sold')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('izdelek', 'recipient_email', 'date', 'status')
    form = OrderModelForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
