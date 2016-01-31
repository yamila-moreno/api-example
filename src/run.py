import click
import pytest

from server import DEFAULT_PORT


@click.group()
def cli():
    pass


@cli.command()
@click.option('-o', is_flag=False, default="", help='pytest options')
def test(o):
    """Test the application"""
    pytest.main('-s {0}'.format(o))


@cli.command()
@click.option('--create-db', is_flag=True, help='creates a new database')
@click.option('--with-fixtures', is_flag=True, help='loads fixtures')
@click.option('--port', default=DEFAULT_PORT, help='port where the api is served. Default={}'.format(DEFAULT_PORT))
@click.option('--hot-reload/--no-hot-reload', default=True, is_flag=True,
              help='reload server when there is a change on code. Must be disabled in order to use --create-db or --with-fixtures. Default True')
def serve(create_db, with_fixtures, port, hot_reload):
    """Serve the application"""
    from server import serve
    serve(create_db, with_fixtures, port, hot_reload)


if __name__ == '__main__':
    cli()
