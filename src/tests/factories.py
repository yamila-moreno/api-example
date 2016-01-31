import uuid
from random import randint

from faker import Faker

from entities.user import User as UserE
from repositories import user

fake = Faker()


################
#     USER     #
################

def build_user(**kwargs):
    userE = UserE(
            uuid=kwargs.get('uuid', uuid.uuid4().hex),
            email=kwargs.get('email', fake.email()),
            password='abc12345',
            enabled=True)
    return userE


def create_user(**kwargs):
    userE = user.create_user(
            uuid=kwargs.get('uuid', uuid.uuid4().hex),
            email=kwargs.get('email', fake.email()),
            password='abc12345',
            enabled=True)
    return userE
