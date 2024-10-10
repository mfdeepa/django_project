from django.contrib import admin
from django.urls import path

from productService.admin import ProductAdmin, CategoryAdmin
from productService.views.product_views import ProductListCreateAPIView

urlpatterns = [
    path("", ProductAdmin),
    path("cat/", CategoryAdmin),
    path("products/", ProductListCreateAPIView.as_view()),
]
