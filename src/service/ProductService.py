from src.model.Product import Product
from src.repositories.ProductRepository import add_product, list_product

def add(name: str, description: str) -> Product:
    if(name is None or name == '' or description is None or description == ''):
        raise Exception

    return add_product(name, description)

def lister() -> Product:
    return list_product()