from src.model.Product import Product, db
import sqlalchemy

def add_product(name: str, description: str) -> Product:
    product = Product(name=name, description=description)
    db.session.add(product)
    db.session.commit()

    return product

def list_product() -> sqlalchemy.orm.query.Query:
    products = db.session.query(Product).all()
    return products

def get_product(id: int) -> sqlalchemy.orm.query.Query:
    product = db.session.query(Product).get(id)
    return product