#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")


    @property
    def cities(self):
            """returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City"""
            dict_cities = storage.all(City)
            list_cities = []

            for value in dict_cities.keys():
                list_cities.append(value)

                return list_cities
