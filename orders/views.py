from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from orders.forms import OrderForm
from orders.models import Product, Order
from utils.costumers import create_order, send_email

def success(request):
    return render(request, 'success.html')

def index(request):
    last_products = Product.objects.all().order_by('-id')[:3]
    all_products = Product.objects.all()
    return render(request, 'index.html', {'last_products': last_products, 'all_products': all_products})


def products(request, pk):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = create_order(form, pk)

            send_email(order)

            return redirect('success')
        else:
            product = get_object_or_404(Product, id=pk)
            return render(request, 'product.html', {'product': product, 'form': form})
    else:
        product = get_object_or_404(Product, id=pk)
        form = OrderForm()
        return render(request, 'product.html', {'product': product, 'form': form})
