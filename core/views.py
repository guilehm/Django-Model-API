from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

# Create your views here.
def api(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'core/API.html', context)


class ProductDetail(APIView):
    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)
        print('produto aqui *****', product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
