import json
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.ClientService import add, lister
from flask import Flask, request, jsonify 
from flask_apispec import marshal_with
import re
from marshmallow import Schema, ValidationError, fields, validates

def isValidCPF(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])


class ClientValidator(Schema):
    name = fields.Str(required=True)
    cpf = fields.Str()
    
    @validates("cpf")
    def validate_name(self, value):
        if not isValidCPF(value):
           raise ValidationError({ "error": "CPF não é valido"})

    @validates("name")
    def validate_name(self, value):
        if len(value) < 10:
           raise ValidationError({ "error": "O nome do cliente deve ter no mínimo 10 caracteres"})

class Client( Resource):
    def post(self):
        try:
            data = request.get_json()
            schema = ClientValidator()
            errors = schema.validate(data)

            if errors:
                raise ValidationError(errors)
            
            client = add(**data)

            return client.toDict(), 201
        except ValidationError as err:
            return err.messages, 400
        except OperationalError:
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


