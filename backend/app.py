from flask import Flask  
from flask_restful import Api
from src.routes.endpoints import initialize_endpoints
from src.model.dbmodel import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/pav'

    db.init_app(app)
    
    # Flask API
    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app