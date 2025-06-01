from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from src.model.dbmodel import db
from sqlalchemy import inspect

class Product(db.Model):
    __tablename__ = "product"

    # Columns
    id          = Column("id",Integer,primary_key=True)
    name        = Column("name", String(150), nullable=False)
    description = Column("description", String(1000), nullable=False)

    def toDict(self):
       return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
