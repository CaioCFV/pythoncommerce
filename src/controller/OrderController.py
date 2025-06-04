from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.OrderService import add, lister
from flask import Flask, request
from marshmallow import Schema, ValidationError, fields

class OrderVariant(Schema):
    client_id   = fields.Int(required=True)
    variants    = fields.List(fields.Int(), required=True)


class Order(Resource):
    def post(self):
        try:
            data = request.get_json()
            schema = OrderVariant()
            errors = schema.validate(data)

            if errors:
                raise ValidationError(errors)

            order = add(**data)

            print(order)
            
            return order, 200

        except ValidationError as err:
            return err.messages, 400
        except OperationalError:
            abort(500, message="Internal Server Error")


