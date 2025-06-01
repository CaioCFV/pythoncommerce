from src.model.Client import Client
from src.repositories.ClientRepository import add_client, list_client

def add(name: str, cpf: str) -> Client:
    return add_client(name, cpf)

def lister() -> Client:
    return list_client()