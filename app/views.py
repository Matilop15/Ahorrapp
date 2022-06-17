from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONparser
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from app.models import Product, SuperMarkets, ProductMarket
from app.serializers import ProductMarketSerializer, ProductSerializer
from app.serializers import SuperMarketsSerializer

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


@api_view()
def product_market_api(request, id=0):
    """ProductMarket api"""
    if request.method == 'GET':
        product_market = ProductMarket.objects.all()
        product_market_serializer = ProductMarketSerializer(product_market,
                                                    many=True)
        return Response(product_market_serializer.data)


@api_view()
def super_markets_api(request, id=0):
    """SuperMarket api"""
    if request.method == 'GET':
        super_markets = SuperMarkets.objects.all()
        super_markets_serializer = SuperMarketsSerializer(super_markets,
                                                    many=True)
        return Response(super_markets_serializer.data)
