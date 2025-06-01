from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.VariantService import add, lister
from flask import Flask, request


class Variant(Resource):
    def post(self):
        try:
            data = request.json
            variant = add(data['name'], data['ean'], data['quantity'], data['price'], data['product_id'])
            return {
                'id': variant.id, 
                'name': variant.name, 
                'ean': variant.ean, 
                'quantity': variant.quantity, 
                'price': variant.price,
                'product_id': variant.product_id
                }, 201

        except (OperationalError, IntegrityError):
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


