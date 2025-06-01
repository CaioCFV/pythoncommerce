from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.ProductService import add, lister
from flask import Flask, request


class Product(Resource):
    def post(self):
        try:
            data = request.json
            product = add(data['name'], data['description'])
            return {'id': product.id, 'name': product.name, 'description': product.description}, 201

        except (OperationalError, IntegrityError):
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


