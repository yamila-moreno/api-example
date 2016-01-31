from unittest.mock import patch

from bcrypt import hashpw, gensalt

from services.user import login, register, list
from tests.factories import build_user


def test_login_ok():
    password = "aaa"
    with patch('services.user.get_user_by_email') as mock:
        user = build_user()
        user.password = hashpw(password, gensalt())
        mock.return_value = user
        ok, data, errors = login("a@a.com", password)
        assert mock.call_count == 1
        assert ok is True
        assert 'token' in data


def test_login_fail():
    password = "aaa"
    with patch('services.user.get_user_by_email') as mock:
        user = build_user()
        user.password = hashpw(password, gensalt())
        mock.return_value = user
        ok, data, errors = login("a@a.com", "bbb")
        assert mock.call_count == 1
        assert ok is False
        assert 'email' in errors


def test_register_ok():
    user = build_user()
    with patch('services.user.get_user_by_email') as mock_get_user:
        with patch('services.user.create_user') as mock_create_user:
            with patch('services.user.send_email') as mock_send_email:
                mock_get_user.return_value = None
                mock_create_user.return_value = user

                ok, data, errors = register("a@a.com", "aaa")
                assert mock_create_user.call_count == 1
                assert mock_send_email.call_count == 1
                assert ok is True
                assert 'user' in data


def test_register_fail():
    user = build_user()
    with patch('services.user.get_user_by_email') as mock_get_user:
        with patch('services.user.create_user') as mock_create_user:
            with patch('services.user.send_email') as mock_send_email:
                mock_get_user.return_value = user

                ok, data, errors = register("a@a.com", "aaa")
                assert mock_create_user.call_count == 0
                assert mock_send_email.call_count == 0
                assert ok is False
                assert 'email' in errors
