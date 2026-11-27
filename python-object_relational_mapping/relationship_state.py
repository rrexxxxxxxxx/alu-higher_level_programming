#!/usr/bin/python3
"""Define the State class with a cities relationship, and the Base."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """A state, stored in the states table, linked to its cities."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan",
                          order_by="City.id")
