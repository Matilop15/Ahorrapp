from django.urls import re_path
from app import views


urlpatterns = [
    re_path(r'^api/product/', views.product_api),
    re_path(r'^api/product/([0-9]+)$', views.product_api),
    re_path(r'^api/productmarket/$', views.product_market_api),
    re_path(r'^api/productmarket/([0-9]+)$', views.product_market_api),
    re_path(r'^api/supermarket/$', views.super_markets_api),
    re_path(r'^api/supermarket/([0-9]+)$', views.super_markets_api),
]
