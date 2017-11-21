from django import forms
from django.contrib import admin

# Register your models here.
from orders.models import Product, Order


class ProductModelForm(forms.ModelForm):
    description = forms.CharField(label='Opis', widget=forms.Textarea)
    short_description = forms.CharField(label='Kratek opis(max 50 znakov)', widget=forms.Textarea)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('fotografija', 'name', 'size', 'price', 'sold')
    form = ProductModelForm


class OrderAdmin(admin.ModelAdmin):
    list_display = ('izdelek', 'recipient_email', 'date', 'status')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
