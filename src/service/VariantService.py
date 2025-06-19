from src.model.Variant import Variant
from src.repositories.VariantRepository import add_variant, list_variant, get_variant_by_ean
from src.repositories.ProductRepository import get_product
from marshmallow import  ValidationError

def add(name: str, ean: str, quantity: int, price: int, product_id: int) -> Variant:
    product = get_product(product_id)
    variant = get_variant_by_ean(ean)

    if not product:
        raise ValidationError({ "field": {"error":"produto não encontrado"}})
    
    if variant:
        raise ValidationError({ "field": {"error":"codigo ean já cadastrado ou inválido"}})

    return add_variant(name, ean, quantity, price, product_id)

def lister() -> Variant:
    return list_variant()

