import json
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.ClientService import add, lister
from flask import Flask, request, jsonify 
from flask_apispec import marshal_with

class Client( Resource):
    def post(self):
        try:
            data = request.json
            client = add(data['name'], data['cpf'])
            return {'id': client.id, 'name': client.name, 'cpf': client.cpf}, 201

        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")
    
    def get(self):
        try:            
            response = lister()
            clients = []
            for client in response:
                clients.append(client.toDict())
            return clients, 200

        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


