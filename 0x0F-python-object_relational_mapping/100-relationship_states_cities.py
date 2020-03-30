#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    meta = MetaData(engine)
    Session = sessionmaker(bind=engine)

    tStates = Table('states', meta,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(128)))

    tCities = Table('cities', meta,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(128)),
                    Column('state_id', Integer, nullable=True))

    tStates.create()
    tCities.create()

    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
