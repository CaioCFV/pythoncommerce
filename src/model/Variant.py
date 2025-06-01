from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from src.model.dbmodel import db
from sqlalchemy import inspect

class Variant(db.Model):
    __tablename__ = "variant"

    # Columns
    id         = Column("id",Integer,primary_key=True)
    name       = Column("name", String(150), nullable=False)
    ean        = Column("ean", String(150), nullable=False)
    quantity   = Column("quantity",Integer, nullable=False)
    price      = Column("price", Integer, nullable=False)
    product_id = Column("product_id", ForeignKey("product.id"), nullable=False)

    def toDict(self):
       return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
