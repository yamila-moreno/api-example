import sys

from anillo.app import application
from anillo.handlers.routing import router
from anillo.middlewares.json import wrap_json_body, wrap_json_response
from anillo.utils.common import chain
from anillo_auth.auth import wrap_auth

from settings.base import config
from urls import urls
from utils.authorization import backend as auth_backend
from utils.middlewares.cors import wrap_cors_response
from utils.middlewares.sqlalchemy import wrap_sqlalchemy_session

DEFAULT_PORT = config.getint('server', 'port')
DEFAULT_HOST = config.get('server', 'host')


def setup_app():
    main_handler = chain(
            wrap_auth(backend=auth_backend),
            wrap_json_body,
            wrap_json_response,
            wrap_cors_response,
            wrap_sqlalchemy_session,
            router(urls)
    )

    return application(main_handler)


def init_db():
    from repositories.config import Base, engine
    Base.metadata.create_all(engine)


def fixtures():
    from services.fixtures import load_fixtures
    load_fixtures()


def serve(create_db, with_fixtures, port, hot_reload):
    if create_db:
        if hot_reload:
            sys.exit("You must use the flag --no-hot-reload in order to create the database")
        init_db()
    if with_fixtures:
        if hot_reload:
            sys.exit("You must use the flag --no-hot-reload in order to load fixtures")
        fixtures()
    app = setup_app()
    from anillo import serving
    serving.run_simple(
            app,
            port=port,
            host=DEFAULT_HOST,
            autoreload=hot_reload)
