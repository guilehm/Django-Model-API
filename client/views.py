from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request,'client/index.html')


def products(request):
    products = requests.get('http://localhost:8000/api/products').json()
    context = {
        'products' : products,
    }
    return render(request,'client/products.html', context)