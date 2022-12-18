from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from dataBases.creation import ActivityTable

engine = create_engine("sqlite:///activityBase.db")
session = Session(bind=engine)


def add_user(tg_iD,second_namE,first_namE):
    session.connection()
    some_user = ActivityTable(
        tg_id = tg_iD,
        second_name = second_namE,
        first_name = first_namE,
        activity = 0,
        mark_tests = 0
    )
    session.add(some_user)
    session.commit()
    session.close()
