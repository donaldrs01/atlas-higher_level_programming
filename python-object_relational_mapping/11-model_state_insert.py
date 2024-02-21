#!/usr/bin/python3
"""Adds the State object 'Louisiana' to hbtn_0e_6_usa database
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

    #  create new State object for Louisiana
    new_state = State(name='Louisiana')
    #  add State object to session
    session.add(new_state)
    #  commit to database
    session.commit()
    #  print state.id
    print(new_state.id)

    session.close()
