#!/usr/bin/python3
"""
Script that lists all State objects present in 'states' table
of hbtn_0e_6_usa database

Usage: 
    python3 7-model_state_fetch_all.py <username> <pw> <db>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    
    #  assign args to variables
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    #  connect to MySQL server
    engine = create_engine(f'mysql+mysqldb://{user}:{pw}@localhost:3306/{db}')

    #  Bind metadata (property of base class) to the engine
    #  Allows us to interact with database
    Base.metadata.bind = engine

    #  create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    #  Query all State objects
    all_states = session.query(State).order_by(State.id).all()

    #  Print results in proper format
    for state in all_states:
        print(f"{state.id}: {state.name}")

    #  Close session
    session.close()
