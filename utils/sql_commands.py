from sqlalchemy.exc import IntegrityError

from utils.datbase import session
from utils.schemas import User


def register_user(user_id: int):
    user = User(
        user_id=user_id
    )
    session.add(user)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def select_users():
    users = session.query(User).all()
    return users


def add_coin_user(tg_id, count):
    user = session.query(User).filter(
        User.user_id.like(tg_id)
    ).all()[0]
    if user.coins:
        user.coins += count
    else:
        user.coins = count
    session.add(user)
    session.commit()


def get_user(tg_id):
    user = session.query(User).filter(
        User.user_id.like(tg_id)
    ).all()[0]
    return user
