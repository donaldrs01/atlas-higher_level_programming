#!/usr/bin/python3
"""Updates 'states' table to change name of State object where id=2
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
    #  query states table and searches for first result where state.id = 2
    update_state = session.query(State).filter(State.id == 2).first()

    update_state.name = 'New Mexico'

    session.commit()

    session.close()
