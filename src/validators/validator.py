from functools import wraps

from anillo.http import BadRequest
from skame.validator import validate


class Validator:
    __schema__ = None
    key_name = None

    def __init__(self, data: dict):
        (self.cleaned_data, self.errors) = self.validate(data)

    def validate(self, data):
        return validate(self.__schema__, data)


def with_validators(validator_list):
    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(instance, request, **kwargs):
            data, errors = {}, {}
            body = 'body' in request and request.body or {}
            # To get the url params
            body.update(kwargs)
            for validator_class in validator_list:
                validator = validator_class(body)
                if validator.errors:
                    errors.update(validator.errors)
                data[validator.key_name] = validator

            if errors:
                return BadRequest(errors)

            return func(instance, request, data)

        return returned_wrapper

    return func_wrapper
