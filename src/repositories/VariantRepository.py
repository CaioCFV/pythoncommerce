from src.model.Variant import Variant, db
import sqlalchemy

def add_variant(name: str, ean: str, quantity: int, price: int, product_id: int) -> Variant:
    variant = Variant(name=name, ean=ean, quantity=quantity, price=price, product_id=product_id)
    db.session.add(variant)
    db.session.commit()

    return variant

def list_variant() -> sqlalchemy.orm.query.Query:
    variants = db.session.query(Variant).all()
    return variants

def get_variant(id: int) -> sqlalchemy.orm.query.Query:
    variant = db.session.query(Variant).get(id)
    return variant

def decrement_variant(id: int) -> sqlalchemy.orm.query.Query:
    variant = db.session.query(Variant).get(id)
    variant.quantity = variant.quantity - 1
    db.session.commit()
    
    return variant