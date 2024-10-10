from rest_framework import serializers

from productService.models import Product
from productService.seralizers.ratingSerializer import RatingSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category']
