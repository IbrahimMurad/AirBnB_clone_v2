#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, orm, Table
from models import storage
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)
    amenity_ids = []

    reviews = orm.relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")

    place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)

    amenities = orm.relationship("Amenity", secondary="place_amenity", viewonly=False)

    @property
    def reviews(self):
        """getter attribute that returns a list of Review instances
with place_id equals to the current Place.id"""
        from models.review import Review
        place_reviews = []
        for rev in storage.all(Review).values():
            if rev.place_id == self.id:
                place_reviews.append(rev)
        return place_reviews

    @property
    def amenities(self):
        """getter attribute that returns the list of Amenity instances
based on the attribute amenity_ids that contains all Amenity.id linked to the Place"""
        from models.amenity import Amenity
        place_amenities = []
        for amenity in storage.all(Amenity).values():
            if amenity.place_id == self.id:
                place_amenities.append(amenity)
        return place_amenities

    @amenities.setter
    def amenities(self, value=None):
        """setter attribute for amenities"""
        from models.amenity import Amenity
        if type(value) is Amenity:
            if value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)