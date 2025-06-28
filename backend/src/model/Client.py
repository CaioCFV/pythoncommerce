from sqlalchemy import create_engine
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.model.dbmodel import db
from sqlalchemy import inspect

class Client(db.Model):
    __tablename__ = "client"

    id   = db.Column("id",Integer,primary_key=True)
    name = db.Column("name", String(150), nullable=False)
    cpf  = db.Column("cpf", String(150), nullable=False)

    def toDict(self):
       return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


