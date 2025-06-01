from src.model.Client import Client
from src.repositories.ClientRepository import add_client, list_client

def add(name: str, cpf: str) -> Client:
    if(name is None or name == '' or cpf is None or cpf == ''):
        raise Exception

    return add_client(name, cpf)

def lister() -> Client:
    return list_client()