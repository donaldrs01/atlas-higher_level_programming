#!/usr/bin/python3
"""Prints the state.id of a State object passed as an argument
from the hbtn_0e_6_usa database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}')

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()
    #  searches for state_name entry in database
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
