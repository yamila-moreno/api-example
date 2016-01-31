import functools

from repositories.session import session_manager


def wrap_sqlalchemy_session(
        func=None,
        *,
        allow_origin='*',
        allow_headers=set(["Origin", "X-Requested-With", "Content-Type", "Accept"])):
    """
    A middleware that creates a sqlalchemy session at the start of the request, and close it at the end.
    If there isn't an exception on the execution, the session is commited. Otherwise, it is rollbacked.
    """

    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        session_manager.create_session()
        try:
            response = func(request, *args, **kwargs)
            session_manager.commit_session()
        except:
            session_manager.rollback_session()
            raise
        finally:
            session_manager.close_session()

        return response

    return wrapper
