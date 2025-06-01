from src.model.Variant import Variant
from src.repositories.VariantRepository import add_variant, list_variant

def add(name: str, ean: str, quantity: int, price: int, product_id: int) -> Variant:
    if( name is None or name == '' 
        or ean is None or ean == '' 
        or quantity is None or quantity == ''
        or price is None or price == ''
        or product_id is None or product_id == ''
    ):
        raise Exception

    return add_variant(name, ean, quantity, price, product_id)

def lister() -> Variant:
    return list_variant()

