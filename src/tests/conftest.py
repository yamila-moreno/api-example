import pytest
from sqlalchemy_utils import database_exists, create_database, drop_database

from repositories.config import Base
from repositories.config import engine
from repositories.session import session_manager


@pytest.fixture(scope="session", autouse=True)
def create_db(request):
    print("\n===> Create and synchro database")

    # drop database if exist
    if database_exists(engine.url):
        drop_database(engine.url)

    # create a new database for testing purposes
    create_database(engine.url)

    # setting the new database
    Base.metadata.create_all(engine)

    def drop_db():
        print("\n===> Drop database")
        # dropdb at the end of the session
        drop_database(engine.url)

    request.addfinalizer(drop_db)


@pytest.fixture(scope="function", autouse=True)
def create_session_and_trunc_tables(request):
    session_manager.create_session()
    trunc_all_tables()

    def end_session():
        session_manager.commit_session()
        session_manager.close_session()

    request.addfinalizer(end_session)


def trunc_all_tables():
    from repositories.config import metadata
    for table in reversed(metadata.sorted_tables):
        session_manager.session.execute(table.delete())
