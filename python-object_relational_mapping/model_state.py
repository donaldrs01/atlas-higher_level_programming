#!/usr/bin/python3
"""Defines 'state' class using SQLAlchemy
Also creates an instance 'Base' of the declarative_base() class
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):