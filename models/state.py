#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", back_populates="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter for the list of City instances corresponding to this
            state """
            from models import storage
            cities_list = []
            return [cities_list.append(city) for city in storage.all(City).values()
                    if self.id == city.state_id]
