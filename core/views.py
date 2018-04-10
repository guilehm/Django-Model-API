from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import ProductSerializer

# Create your views here.
def api(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'core/API.html', context)


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        context = {'request': request}
        serializer = ProductSerializer(products, context=context, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)
        context = {'request': request}
        serializer = ProductSerializer(product, context=context)
        return Response(serializer.data)
