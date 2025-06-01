from src.model.Order import Order, db
from src.model.OrderVariant import OrderVariant, db as dbvariant
import sqlalchemy
from src.repositories.VariantRepository import get_variant, decrement_variant

def add_order(client_id, variants) -> Order:
    total = 0
    variantIDS = []
    variantsF = []

    for id in variants:
        variant = get_variant(id)
        if(variant and variant.quantity > 0):
            decrement_variant(variant.id)
            total += variant.price
            variantIDS.append(variant.id)
            variantsF.append(variant.toDict())

    order = Order(total=total, client_id=client_id)
    db.session.add(order)
    db.session.commit()

    print(order.id)

    for id in variantIDS:
        orderVariant = OrderVariant(order_id=order.id, variant_id=id)
        dbvariant.session.add(orderVariant)
        dbvariant.session.commit()

    print(total)

    return {
        'order_id': order.id,
        'client_id': client_id,
        'variants': variantsF,
        'total': total
    }

def list_order() -> sqlalchemy.orm.query.Query:
    order = db.session.query(Order).all()
    return order