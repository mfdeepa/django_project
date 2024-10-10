from abc import ABC, abstractmethod


class CategoryService(ABC):
    @abstractmethod
    def get_all_categories(self) -> str:
        pass

    @abstractmethod
    def get_product_in_category(self) -> str:
        pass
