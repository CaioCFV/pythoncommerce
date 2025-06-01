from src.model.Client import Client, db
import sqlalchemy

def add_client(name: str, cpf: str) -> Client:
    client = Client(name=name, cpf=cpf)
    db.session.add(client)
    db.session.commit()

    return client

def list_client() -> sqlalchemy.orm.query.Query:
    clients = db.session.query(Client).all()
    return clients