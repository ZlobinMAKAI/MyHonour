from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from dataBases.creation import ActivityTable


engine = create_engine("sqlite:///activityBase.db")
session = Session(bind=engine)

def getId(tg_iD):
    t_id =  session.query(ActivityTable.id).filter(ActivityTable.tg_id==tg_iD).all()[0][0]
    return t_id

def getTg_id(tg_iD):
    return tg_iD

def getSecond_name(tg_iD):
    s_name =  session.query(ActivityTable.second_name).filter(ActivityTable.tg_id==tg_iD).all()[0][0]
    return s_name

def getFirst_name(tg_iD):
    f_name = session.query(ActivityTable.first_name).filter(ActivityTable.tg_id == tg_iD).all()[0][0]
    return f_name

def getActivity(tg_iD):
    act_points = session.query(ActivityTable.activity).filter(ActivityTable.tg_id == tg_iD).all()[0][0]
    return act_points

def getTest_mark(tg_iD):
    test_mark = session.query(ActivityTable.mark_tests).filter(ActivityTable.tg_id == tg_iD).all()[0][0]
    return test_mark