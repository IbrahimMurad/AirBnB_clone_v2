#!/usr/bin/python3
"""This module defines a class User"""

from sqlalchemy import Column, String, orm
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = orm.relationship("Place", cascade="all, delete, delete-orphan",
                              backref="user")

    reviews = orm.relationship("Review", cascade="all, delete, delete-orphan",
                               backref="user")
