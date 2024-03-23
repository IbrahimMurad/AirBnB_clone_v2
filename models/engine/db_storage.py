#!/usr/bin/python3
"""This module creates a new engine for the project"""

from sqlalchemy import create_engine, MetaData, orm
import os


class DBStorage:
    """ This class is a second engine for the project """
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}\
'.format(user, pswd, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            MetaData(bind=self.__engine).drop_all()

    def all(self, cls=None):
        """query on the current database session
all objects depending of the class name cls"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = [BaseModel, User, Place, State, City, Amenity, Review]

        all_obj_dict = {}
        if not cls:
            for _cls in classes:
                _cls_objs = self.__session.query(_cls).all()
                for obj in _cls_objs:
                    all_obj_dict.update({obj.to_dict()['__class__']
                                         + '.' + obj.id: obj})
        else:
            _cls_objs = self.__session.query(cls).order_by("name").all()
            for obj in _cls_objs:
                all_obj_dict.update({obj.to_dict()['__class__']
                                     + '.' + obj.id: obj})
        return all_obj_dict

    def new(self, obj):
        """add the obj to the current db session"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session"""

        self.__session.commit()

    def delete(self, obj=None):
        """deletes the obj from the current db session"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

        from models.base_model import Base
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session_factory = orm.sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
        thread_safe_session = orm.scoped_session(Session_factory)
        self.__session = thread_safe_session()

    def close(self):
        """closes the current session"""
        self.__session.close()
