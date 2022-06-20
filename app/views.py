from urllib import request
from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import SuperMarketSerializer, product_listSerializer, productSerializer
from .models import product, product_list, market
""" Defines views """


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ Product View Set """
    serializer_class = productSerializer
    queryset = product.objects.all()


class SuperMarketViewSet(viewsets.ReadOnlyModelViewSet):
    """ Super Market View Set """
    serializer_class = SuperMarketSerializer
    queryset = market.objects.all()


class ProductMarketViewSet(viewsets.ReadOnlyModelViewSet):
    """ Product Market View set """
    serializer_class = product_listSerializer
    queryset = product_list.objects.all()


# class AllProductsViewSet(viewsets.ViewSet):
    # """ All products from a supermarket"""

    # def retrieve(self, request, *args, **kwargs):
        # queryParams = self.request.GET.get('abc')
        # inner_qs = ProductMarket.objects.filter(SuperMarketId_id=queryParams)
        # entries = Product.objects.filter(ProductId__in=inner_qs)
        # queryset = Product.objects.filter(ProductId = queryParams)
        # serializer = PlayerSerializer(queryset)
        # return Response(serializer.data)

