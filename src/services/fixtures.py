from repositories.session import session_manager
from repositories.user import create_user


def load_fixtures():
    session_manager.create_session()

    _load_users_fixtures()

    session_manager.commit_session()
    session_manager.close_session()


def _load_users_fixtures():
    create_user('jimena@test.com', 'abc12345', '8c99f50fcb424c66b6e489d15461b782')
    create_user('nikolai@test.com', 'abc12345', '9942eb5913c54f2eae5353e6b43324fb')
