from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'validate'}))
    comment = forms.CharField(required=False)

    class Meta:
        model = Order
        fields = ('email', 'comment')