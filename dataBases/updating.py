from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Session, sessionmaker
from dataBases.creation import ActivityTable
from dataBases.deleter import deleteUser
from dataBases.getValue import getTest_mark, getFirst_name, getSecond_name, getActivity

engine = create_engine("sqlite:///activityBase.db")
session = Session(bind=engine)

def updateUser(tg_iD, second_namE, first_namE,activitY,mark_testS):
    deleteUser(tg_iD)
    session.connection()
    some_user = ActivityTable(
        tg_id=tg_iD,
        second_name=second_namE,
        first_name=first_namE,
        activity=activitY,
        mark_tests=mark_testS
    )
    session.add(some_user)
    session.commit()
    session.close()

def activityMark(tg_iD):
    session.connection()

    SN = getSecond_name(tg_iD)
    FN = getFirst_name(tg_iD)
    MK = getTest_mark(tg_iD)

    activityP = session.query(ActivityTable.activity).filter(ActivityTable.tg_id==tg_iD).all()[0][0]
    activityP +=1

    updateUser(tg_iD,SN,FN,activityP,MK)
    session.commit()
    session.close()

def testMark(tg_iD,MarkTest):
    session.connection()

    SN = getSecond_name(tg_iD)
    FN = getFirst_name(tg_iD)
    AK = getActivity(tg_iD)

    updateUser(tg_iD, SN, FN, AK, MarkTest)
    session.commit()
    session.close()


