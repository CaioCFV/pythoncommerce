from src.model.Product import Product
from src.repositories.ProductRepository import add_product, list_products

def add(name: str, description: str) -> Product:
    return add_product(name, description)

def lister() -> Product:
    return list_products()