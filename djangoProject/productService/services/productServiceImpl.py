from typing import Optional, List

import httpx
import injector

from productService.clients.fakeStoreClient.fakeStoreClient import FakeStoreClient
from productService.models import Product, Category
from productService.seralizers.productSerializer import ProductSerializer
from productService.services.product_service import ProductService


class ProductServiceImpl(ProductService):

    @injector.inject
    def __init__(self):
        self.http_client = httpx.Client
        self.fake_store_client = FakeStoreClient()

    @injector.inject
    def convert_fake_store_product_data_to_product(self, product_data: dict) -> Product:
        category_name = product_data.get('category', 'Unknown')
        category, created = Category.objects.get_or_create(name=category_name)

        # Convert external API data to your Django model instance
        product = Product.objects.create(
            title=product_data['title'],
            price=product_data['price'],
            description=product_data.get('description', ''),
            # description='description',
            category=category,
        )
        return product

    def get_all_products(self) -> List[Product]:
        # Get product data from the external API
        fake_store_products = self.fake_store_client.get_all_products()

        # Convert the data into Product instances
        answer = []
        for product_data in fake_store_products:
            answer.append(self.convert_fake_store_product_data_to_product(product_data))

        return answer

    def get_single_product(self, product_id: int) -> Optional[Product]:
        pass

    def add_new_product(self, product: ProductSerializer) -> Product:
        pass

    def update_product(self, product_id: int, product: Product) -> Product:
        pass

    def delete_product(self, product_id: int) -> bool:
        pass

    def get_limit_product_result(self, product_id: int) -> str:
        pass

    def update_product_partially(self, product_id: int) -> str:
        pass

    def get_product_by_sorting(self, product_id: int) -> str:
        pass

    def replace_product(self, product_id: int, product: Product) -> Product:
        pass
