from .config import DBSession


class SessionManager:
    def __init__(self, *args, **kwargs):
        self.session = None

    def create_session(self):
        self.session = DBSession()
        return self.session

    def close_session(self):
        self.session.close()

    def commit_session(self):
        self.session.commit()

    def rollback_session(self):
        self.session.rollback()


session_manager = SessionManager()
