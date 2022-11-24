#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
hbnb_dev_db.users= [["user"]]
class User(BaseModel.Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String[128], nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")
