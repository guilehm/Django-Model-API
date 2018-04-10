from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Product
from core.serializers import ProductSerializer

# Create your views here.
def index(request):
    return render(request,'client/index.html')


def products(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'client/products.html', context)


def api(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'client/API.html', context)