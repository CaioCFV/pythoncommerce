from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from src.model.dbmodel import db
from sqlalchemy import inspect

class Order(db.Model):
    __tablename__ = "order"

    # Columns
    id         = Column("id",Integer,primary_key=True)
    total      = Column("total", Integer, nullable=False)
    client_id  = Column("client_id", ForeignKey("client.id"), nullable=False)

    def toDict(self):
       return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
