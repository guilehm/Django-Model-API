from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request,'client/index.html')


def products(request):
    products = requests.get('http://localhost:8000/api/products').json()
    context = {
        'products' : products,
    }
    return render(request,'client/products.html', context)


def product(request, product_slug):
    product = requests.get('http://localhost:8000/api/products/' + product_slug).json()
    print(product)
    context = {
        'product' : product,
    }
    return render(request,'client/product.html', context)