import bcrypt

from errors.errors import get_response_error
from repositories.user import get_user_by_email, create_user, get_user_by_uuid, get_users
from utils.authorization import generate_token
from utils.token import generate_and_encrypt_token


def login(email, password):
    errors = {}

    user = get_user_by_email(email)

    if not user or not user.enabled:
        errors["email"] = get_response_error("WRONG_EMAIL")
    if errors:
        return False, None, errors

    return execute_login(user, password)


def execute_login(user, password):
    # Check that an unencrypted password matches one that has
    # previously been hashed
    if bcrypt.hashpw(password, user.password) == user.password:
        token = generate_token(user.uuid)
        return True, {"token": token}, None
    else:
        return False, None, {"email": get_response_error("WRONG_EMAIL")}


def register(email, password):
    errors = {}

    user = get_user_by_email(email)

    if user:
        errors["email"] = get_response_error("EMAIL_ALREADY_REGISTERED")
    if errors:
        return False, None, errors

    return execute_register(email, password)


def execute_register(email, password):
    token, token_crypt = generate_and_encrypt_token()
    user = create_user(email, password, token_crypt)

    return True, {"user": user}, None

def list():
    users = get_users()
    return True, {'users': users}, None
