from sqlalchemy import Column, Integer

from utils.datbase import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    coins = Column(Integer)

