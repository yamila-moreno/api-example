from functools import wraps

from anillo.http import Unauthorized
from anillo_auth.backends.token import JWSBackend
from itsdangerous import JSONWebSignatureSerializer

from errors.errors import get_response_error
from settings.base import config

_secret = config.get("login", "secret")
_token_name = "Bearer"


def login_required(func):
    @wraps(func)
    def wrapper(instance, request):
        if request.get('identity') == None:
            return unauthorized()
        else:
            return func(instance, request)

    return wrapper


def unauthorized():
    return Unauthorized({"error": get_response_error("NOT_LOGGED")})


def backend():
    return JWSBackend(secret=_secret, token_name=_token_name)


def generate_token(user_uuid):
    serializer = JSONWebSignatureSerializer(_secret)
    data = serializer.dumps({"user_uuid": user_uuid}).decode("utf-8")
    return "{}: {}".format(_token_name, data)
