#!/usr/bin/python3
"""Prints all 'State' objects that contain the letter 'A' from the hbtn_0e_6_usa database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()
    #  query for State objects containing 'a'
    query = session.query(State).filter(State.name.like('%a%'))
    #  sort results by state.id
    a_states = query.order_by(State.id).all()

    for state in a_states:
        print(f'{state.id}: {state.name}')
    
    session.close()