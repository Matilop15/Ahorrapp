from rest_framework import viewsets
from .serializers import ProductSerializer
from .serializers import ProductMarketSerializer
from .serializers import SuperMarketSerializer
from .models import Product, ProductMarket, SuperMarket
""" Defines views """


class ProductViewSet(viewsets.ModelViewSet):
    """ Product View Set """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SuperMarketViewSet(viewsets.ModelViewSet):
    """ Super Market View Set """
    serializer_class = SuperMarketSerializer
    queryset = SuperMarket.objects.all()


class ProductMarketViewSet(viewsets.ModelViewSet):
    """ Product Market View set """
    serializer_class = ProductMarketSerializer
    queryset = ProductMarket.objects.all()

# class AllProductsViewSet(request):
    # """ All products from a supermarket"""
    # if request.method == 'GET':
