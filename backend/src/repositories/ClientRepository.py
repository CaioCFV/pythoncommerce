from src.model.Client import Client, db
import sqlalchemy

def add_client(name: str, cpf: str):
    client = Client(name=name, cpf=cpf)
    db.session.add(client)
    db.session.commit()

    return client

def list_client():
    clients = db.session.query(Client).all()
    return clients


def get_client(id: int):
    client = db.session.query(Client).get(id)
    return client