from skame.schemas import strings as s, base as b

from errors.errors import get_response_error
from .validator import Validator


class LoginValidator(Validator):
    key_name = 'login_data'
    __schema__ = b.schema({
        'email': s.Email(get_response_error("NOT_AN_EMAIL")),
        'password': s.NotEmpty(get_response_error("CANT_BE_EMPTY"))
    })

    def __init__(self, data: dict):
        super().__init__(data)
        if self.cleaned_data:
            self.email = self.cleaned_data['email']
            self.password = self.cleaned_data['password']


class RegisterValidator(Validator):
    key_name = 'register_data'
    __schema__ = b.schema({
        'email': s.Email(get_response_error("NOT_AN_EMAIL")),
        'password': s.NotEmpty(get_response_error("CANT_BE_EMPTY"))
    })

    def __init__(self, data: dict):
        super().__init__(data)
        if self.cleaned_data:
            self.email = self.cleaned_data['email']
            self.password = self.cleaned_data['password']
