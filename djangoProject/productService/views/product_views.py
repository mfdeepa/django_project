from rest_framework.views import APIView
from rest_framework.response import Response

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
