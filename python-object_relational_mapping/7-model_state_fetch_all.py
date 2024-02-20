#!/usr/bin/python3
"""Script that lists all State objects present in 'states' table
of hbtn_0e_6_usa database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    #  assign args to variables
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]

    #  connect to MySQL server
    eng = create_engine(f'mysql+mysqldb://{user}:{pw}@localhost:3306/{db}')

    #  Bind metadata (property of base class) to the engine
    #  Allows us to interact with database
    Base.metadata.bind = eng

    #  create the session
    Session = sessionmaker(bind=eng)
    session = Session()

    #  Query all State objects
    all_states = session.query(State).order_by(State.id).all()

    #  Print results in proper format
    for state in all_states:
        print(f"{state.id}: {state.name}")

    #  Close session
    session.close()
