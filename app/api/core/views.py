from rest_framework import viewsets
from .serializers import ProductSerializer, SupermarketSerializer
from .models import Product, Supermarket

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    """The viewsets.ModelViewSet provides
    methods to handle CRUD operations by default.
    We just need to do specify the
    serializer class and the queryset."""

class SupermarketViewSet(viewsets.ModelViewSet):
    serializer_class = SupermarketSerializer
    queryset = Supermarket.objects.all()
