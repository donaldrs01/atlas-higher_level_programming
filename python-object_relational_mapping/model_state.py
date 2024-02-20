#!/usr/bin/python3
"""Defines 'state' class using SQLAlchemy
Also creates an instance 'Base' of the declarative_base() class
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create base class that can be inherited by other classes
Base = declarative_base()

class State(Base):
    # Declares that 'state' class is mapped to 'states' database table
    __tablename__ = 'states'

    #  Define columns in 'states' table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')

