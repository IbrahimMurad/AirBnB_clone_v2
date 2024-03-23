#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, orm
from models import storage
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = orm.relationship("City", cascade="all, delete", backref="state")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ getter attribute that returns a list of cities
in the current state
"""
            from models.city import City
            cities_in_state = []
            for city_obj in storage.all(City).values():
                if city_obj.state_id == self.id:
                    cities_in_state.append(city_obj)
            return cities_in_state
