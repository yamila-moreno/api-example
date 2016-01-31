from entities.user import User


def test_tojson_user_ok():
    init_data = {
        'uuid': 'xyz',
        'email': 'xyz@xyz.com',
        'password': 'xyz'
    }
    user = User(**init_data)

    # execute
    json_user = user.toJSONDict()

    # assert
    assert len(json_user) == 2
    assert 'email' in json_user
    assert 'uuid' in json_user
    assert json_user['email'] == init_data['email']
    assert json_user['uuid'] == init_data['uuid']
