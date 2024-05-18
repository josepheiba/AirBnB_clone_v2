#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan", backref="state")

    if models.storage_t != 'db':
        @property
        def cities(self):
            """Getter method for cities when storage is not DBStorage"""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
