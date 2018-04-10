from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request,'core/index.html')


def products(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'core/products.html', context)