from ..database import tables
from .base import Base


class MyModel(Base):
    __table__ = tables.mymodels

    types = tables.MyModelType

    @classmethod
    def create(cls, type):
        return cls(type=type)
