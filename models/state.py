#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage_type
from os import getenv

STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
        if STORAGE_TYPE != "db"
        name = ""
        cities = []
        @property
        def cities(self):
            """returns list of city instances"""
            from models import storage
            related_cities = []
            cities = storage.all(City)

            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
