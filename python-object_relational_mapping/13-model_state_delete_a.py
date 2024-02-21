#!/usr/bin/python3
"""Deletes all State objects from 'states' table that contain the letter 'a'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    #  query for State objects containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    #  delete State objects containing letter 'a'
    for state in states_with_a:
        session.delete(state)

    session.commit()

    session.close()
