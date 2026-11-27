#!/usr/bin/python3
"""Define the State class and the declarative Base for SQLAlchemy."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A state, stored in the states table."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
