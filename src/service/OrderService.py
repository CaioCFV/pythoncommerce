from src.model.Order import Order
from src.repositories.OrderRepository import add_order, list_order
from src.repositories.ClientRepository import get_client
from src.repositories.VariantRepository import get_variant
from marshmallow import  ValidationError

def add(client_id: int, variants) -> Order:
    client = get_client(client_id)

    if not client:
        raise ValidationError("cliente não encontrado")

    for id in variants:
        variant = get_variant(id)
        if(not variant or variant.quantity < 1):
            raise ValidationError("variant não encontrada ou sem estoque")

    return add_order(client_id, variants)

def lister() -> Order:
    return list_order()

