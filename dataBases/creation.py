from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///activityBase.db")
Base = declarative_base()


class ActivityTable(Base):
    __tablename__ = 'users_Xakaton'

    id = Column(Integer, primary_key=True, unique=True)
    tg_id = Column(String(20), unique=True, nullable=False)
    second_name = Column(String(12), nullable=False)
    first_name = Column(String(12), nullable=False)
    activity = Column(Integer, nullable=False)
    mark_tests = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
