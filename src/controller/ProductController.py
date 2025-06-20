from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.ProductService import add, lister
from flask import  request
from marshmallow import Schema, ValidationError, fields, validates, validates_schema
from flask_restful import abort


class ProductValidator(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    
    @validates_schema
    def check_empty(self, data, **kwargs):
        empty_fields = [campo for campo, valor in data.items() if valor in [None, '', []]]
        if empty_fields:
            raise ValidationError({"field": { "error": "não é possivel cadastrar campos vazios"}})
        
    @validates("name")
    def validate_name(self, value):
        if len(value) < 20:
           raise ValidationError({ "error": "O nome do produto deve ter pelo menos 20 caracteres."})



class Product(Resource):
    def post(self):
        try:
            data = request.get_json()
            schema = ProductValidator()
            errors = schema.validate(data)

            if errors:
                raise ValidationError(errors)
            
            product = add(**data)

            return product.toDict(), 201
        except ValidationError as err:
            return err.messages, 400
        except OperationalError:
            abort(500, message="Internal Server Error")



    def get(self):
        try:            
            response = lister()
            products = []
            for product in response:
                products.append(product.toDict())
            return products, 200

        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


