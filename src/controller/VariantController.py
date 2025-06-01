from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.VariantService import add, lister
from flask import Flask, request
from marshmallow import Schema, ValidationError, fields, validates

class VariantValidator(Schema):
    name        = fields.Str(required=True)
    ean         = fields.Int(required=True)
    quantity    = fields.Int(required=True)
    price       = fields.Int(required=True)
    product_id  = fields.Int(required=True)
    
    @validates("price")
    def validate_price(self, value):
        if value <= 0:
           raise ValidationError({ "error": "price não pode ser menor ou igual a zero."})

    @validates("quantity")
    def validate_quantity(self, value):
        if value <= 0:
           raise ValidationError({ "error": "quantity não pode ser menor ou igual a zero."})

class Variant(Resource):
    def post(self):
        try:
            data = request.get_json()
            schema = VariantValidator()
            errors = schema.validate(data)

            if errors:
                raise ValidationError(errors)

            variant = add(**data)

            return variant.toDict(), 201

        except ValidationError as err:
            return err.messages, 400
        except OperationalError:
            abort(500, message="Internal Server Error")
        
    def get(self):
        try:            
            response = lister()
            variants = []
            for variant in response:
                variants.append(variant.toDict())
            return variants, 200

        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


