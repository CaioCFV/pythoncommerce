from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from src.model.dbmodel import db
from sqlalchemy import inspect

class OrderVariant(db.Model):
    __tablename__ = "order_variant"

    # Columns
    id         = Column("id",Integer,primary_key=True)
    variant_id = Column("variant_id", ForeignKey("variant.id"), nullable=False)
    order_id   = Column("order_id", ForeignKey("order.id"), nullable=False)

    def toDict(self):
       return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
