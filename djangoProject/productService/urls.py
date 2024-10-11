from django.contrib import admin
from django.urls import path

from productService.admin import ProductAdmin, CategoryAdmin
from productService.views.product_views import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    path("", ProductAdmin),
    path("cat/", CategoryAdmin),
    path("products/", ProductListCreateAPIView.as_view(), name="product-list"),
    path("products/<product_id>", ProductDetailAPIView.as_view(), name="product_details"),
]
