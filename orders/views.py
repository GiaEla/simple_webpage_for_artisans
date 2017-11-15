from django.shortcuts import render, get_object_or_404

# Create your views here.
from orders.models import Product


def index(request):
    last_products = Product.objects.all().order_by('-id')[:3]
    all_products = Product.objects.all()
    return render(request, 'index.html', {'last_products': last_products, 'all_products': all_products})


def products(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})
