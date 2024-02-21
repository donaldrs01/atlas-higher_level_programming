#!/usr/bin/python3
"""
Script that prints the first 'State' object from hbtn_0e_6_usa database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{pw}@localhost:3306/{db_name}'
    )
    
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id, State.name).first()
    if not first_state:
        print("Nothing")
    else:
        print(f'{first_state.id}: {first_state.name}')
    
    session.close()
