from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, OperationalError
from src.service.OrderService import add, lister
from flask import Flask, request


class Order(Resource):
    def post(self):
        try:
            data = request.json
            order = add(data['client_id'], data['variants'])
            return order, 200

        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


