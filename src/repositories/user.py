import uuid as uuid_generator

from bcrypt import hashpw, gensalt

from entities.user import User
from repositories.persistence import UserTable
from .session import session_manager as sm


def create_user(email, password, uuid=None):
    uuid = uuid if uuid else uuid_generator.uuid4().hex
    user_row = UserTable(
            uuid=uuid,
            email=email,
            password=hashpw(password, gensalt()))
    sm.session.add(user_row)
    sm.session.commit()
    return _user_row_to_user(user_row)


def get_user_by_email(email):
    user_row = _get_user_row_by_filter({"email": email})
    return _user_row_to_user(user_row)


def get_user_by_uuid(uuid):
    user_row = _get_user_row_by_filter({"uuid": uuid})
    return _user_row_to_user(user_row)

def get_users():
    users = sm.session.query(UserTable).all()
    return [_user_row_to_user(user_row) for user_row in users]

def _get_user_by_id(id):
    user_row = sm.session.query(UserTable).get(id)
    return _user_row_to_user(user_row)


def _user_row_to_user(user_row):
    if user_row:
        return User(
                uuid=user_row.uuid,
                email=user_row.email,
                password=user_row.password)
    return None


def _get_user_row_by_filter(f):
    user_row = sm.session.query(UserTable).filter_by(**f).one_or_none()
    return user_row

