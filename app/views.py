from urllib import request
from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import ProductSerializer
from .serializers import ProductMarketSerializer
from .serializers import SuperMarketSerializer
from .models import Product, ProductMarket, SuperMarket
""" Defines views """


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ Product View Set """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SuperMarketViewSet(viewsets.ReadOnlyModelViewSet):
    """ Super Market View Set """
    serializer_class = SuperMarketSerializer
    queryset = SuperMarket.objects.all()


class ProductMarketViewSet(viewsets.ReadOnlyModelViewSet):
    """ Product Market View set """
    serializer_class = ProductMarketSerializer
    queryset = ProductMarket.objects.all()


# class AllProductsViewSet(viewsets.ViewSet):
    # """ All products from a supermarket"""

    # def retrieve(self, request, *args, **kwargs):
        # queryParams = self.request.GET.get('abc')
        # inner_qs = ProductMarket.objects.filter(SuperMarketId_id=queryParams)
        # entries = Product.objects.filter(ProductId__in=inner_qs)
        # queryset = Product.objects.filter(ProductId = queryParams)
        # serializer = PlayerSerializer(queryset)
        # return Response(serializer.data)

