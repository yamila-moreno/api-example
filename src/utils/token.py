import uuid

from bcrypt import hashpw, gensalt


def generate_and_encrypt_token():
    # Generate a uuid as token
    token = uuid.uuid4().hex

    # Cypher the token (in order to not save on db the clear token), and save it
    token_crypt = hashpw(token, gensalt())
    return token, token_crypt
