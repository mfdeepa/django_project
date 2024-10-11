from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from productService.exception.notFoundException import NotFoundException
from productService.seralizers.productSerializer import ProductSerializer
from productService.services.productServiceImpl import ProductServiceImpl


class ProductListCreateAPIView(APIView):

    # @injector.inject
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_ser = ProductServiceImpl()

    def get(self, request):
        products = self.product_ser.get_all_products()
        serialized_products = ProductSerializer(products, many=True).data
        return Response(serialized_products)

    def post(self, request):
        pass


class ProductDetailAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_ser = ProductServiceImpl()

    def get(self, request, product_id):
        try:
            product = self.product_ser.get_single_product(product_id)  # Assume this method exists
            serialized_product = ProductSerializer(product).data
            return Response(serialized_product)
        except NotFoundException:  # Custom exception for not found products
            raise Http404("Product not found.")
