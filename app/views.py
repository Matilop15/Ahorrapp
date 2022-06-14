from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONparser
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from app.models import Product, SuperMarkets, ProductMarket
from app.serializers import ProductMarketSerializer, ProductSerializer, SuperMarketsSerializer
# Create your views here.

@api_view()
def product_api(request, id=0):
    """Product Api"""
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)
    elif request.method == 'POST':
        # product_data = JSONparser().parse(request)
        products_serializer = ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response("Product added successfully")
        return Response("Failed to Add product")
        