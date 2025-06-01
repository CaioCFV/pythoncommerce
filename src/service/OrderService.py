from src.model.Order import Order
from src.repositories.OrderRepository import add_order, list_order

def add(client_id: int, variants) -> Order:
    if( client_id is None or client_id == ''):
        raise Exception

    return add_order(client_id, variants)

def lister() -> Order:
    return list_order()

