from anillo.http.request import Request

from controllers.user import Register, Validate
from repositories.user import create_user


def test_integration_create_user_ok():
    request = Request()
    input_data = {'email': 'abc@xyz.com',
                  'password': 'abc12345'}
    request['body'] = input_data

    # execute
    controller = Register()
    result = controller.post(request)

    assert result['status'] == 200


def test_integration_create_user_fail():
    request = Request()
    input_data = {'email': '',
                  'password': 'abc12345'}
    request['body'] = input_data

    # execute
    controller = Register()
    result = controller.post(request)

    assert result['status'] == 400
    assert result['body']['email']['code'] == "NOT_AN_EMAIL"
