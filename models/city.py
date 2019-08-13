#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=false, ForeignKey("states.id")
