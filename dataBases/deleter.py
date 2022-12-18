from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Session, sessionmaker
from dataBases.creation import ActivityTable

engine = create_engine("sqlite:///activityBase.db")
session = Session(bind=engine)

def deleteUser(tg_iD):
    session.connection()
    user = session.query(ActivityTable).filter(ActivityTable.tg_id == tg_iD).one()
    session.delete(user)
    session.commit()
    session.close()