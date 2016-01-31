import pytest

from errors.errors import get_response_error
from utils.exceptions import ErrorKeyDoesntExistError


def test_error_key_ok():
    error = get_response_error("NOT_LOGGED")
    assert error["code"] == "NOT_LOGGED"
    assert error["message"] == "You need to login"


def test_error_key_error():
    with pytest.raises(ErrorKeyDoesntExistError):
        get_response_error("NOT_LOGGEDDDD")
