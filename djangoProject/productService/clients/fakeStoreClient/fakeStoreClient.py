from typing import List, Optional

import httpx
import injector

from productService.clients.fakeStoreClient.fakeStoreProductSerializer import FakeStoreProductSerializer
from productService.models import Product
from productService.seralizers.productSerializer import ProductSerializer


class FakeStoreClient:
    BASE_URL = "https://fakestoreapi.com"

    @injector.inject
    def __init__(self):
        self.client = httpx.Client()

    def get_all_products(self) -> List[FakeStoreProductSerializer]:
        response = self.client.get(f"{"https://fakestoreapi.com"}/products")  # this will give me json response
        response.raise_for_status()
        product_data = response.json()  # convert json into object
        return product_data

    def get_single_product(self, product_id: int) -> Optional[FakeStoreProductSerializer]:
        pass

    def add_new_product(self, product: ProductSerializer) -> FakeStoreProductSerializer:
        pass

    def update_product(self, product_id: int, product: Product) -> FakeStoreProductSerializer:
        pass

    def delete_product(self, product_id: int) -> FakeStoreProductSerializer:
        pass

    def get_limit_product_result(self, product_id: int) -> FakeStoreProductSerializer:
        pass

    def update_product_partially(self, product_id: int) -> FakeStoreProductSerializer:
        pass

    def get_product_by_sorting(self, product_id: int) -> FakeStoreProductSerializer:
        pass

    def replace_product(self, product_id: int, product: Product) -> FakeStoreProductSerializer:
        pass
