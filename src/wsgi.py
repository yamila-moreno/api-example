from server import setup_app, init_db, fixtures
import sys

def configure_options(*args):
    if 'create-db' in args:
        init_db()

    if 'with-fixtures' in args:
        fixtures()


def load_application(*args):
    configure_options(*args)
    return setup_app()
