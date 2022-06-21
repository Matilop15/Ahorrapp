from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import productViewSet, product_listViewSet, marketViewSet
""" defines URLs """

router = DefaultRouter()
router.register(r'products', productViewSet)
router.register(r'markets', marketViewSet)
router.register(r'product-list', product_listViewSet)

urlpatterns = [
    path("", include(router.urls))
]
