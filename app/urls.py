from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import productViewSet, product_listViewSet, marketViewSet, disco_productsViewSet
""" defines URLs """

router = DefaultRouter()
router.register(r'products', productViewSet)
router.register(r'markets', marketViewSet)
router.register(r'product-list', product_listViewSet)
router.register(r'disco-products', disco_productsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
