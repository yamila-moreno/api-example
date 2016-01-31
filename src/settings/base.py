import configparser
from os import environ
import sys

def set_config_file():
    if 'test' in sys.argv:
        config_file = environ.get('MY_APP_TEST')
        if not config_file:
            raise Exception("You need to set properly MY_APP_TEST variable")
        environ['MY_APP_CONFIG'] = config_file
    else:  # 'serve' in sys.argv or else:
        config_file = environ.get('MY_APP')
        if not config_file:
            raise Exception("You need to set properly MY_APP variable")
        environ['MY_APP_CONFIG'] = config_file


def configure_environment():
    if environ.get('MY_APP_DB_DRIVERNAME'):
        config.set('database', 'drivername', environ.get('MY_APP_DB_DRIVERNAME'))

    if environ.get('MY_APP_DB_HOST'):
        config.set('database', 'host', environ.get('MY_APP_DB_HOST'))

    if environ.get('MY_APP_DB_PORT'):
        config.set('database', 'port', environ.get('MY_APP_DB_PORT'))

    if environ.get('MY_APP_DB_USERNAME'):
        config.set('database', 'username', environ.get('MY_APP_DB_USERNAME'))

    if environ.get('MY_APP_DB_PASSWORD'):
        config.set('database', 'password', environ.get('MY_APP_DB_PASSWORD'))

    if environ.get('MY_APP_DB_DATABASE'):
        config.set('database', 'database', environ.get('MY_APP_DB_DATABASE'))

    if environ.get('MY_APP_SERVER_PORT'):
        config.set('server', 'port', environ.get('MY_APP_SERVER_PORT'))

    if environ.get('MY_APP_LOGIN_SECRET'):
        config.set('login', 'secret', environ.get('MY_APP_LOGIN_SECRET'))


# First, set the config file
set_config_file()

# Second, set the default configuration
config = configparser.ConfigParser()
config_file = environ.get('MY_APP_CONFIG')

if not config_file:
    raise Exception("You need to set properly MY_APP_CONFIG variable")
config.read([config_file])

# Third, set the configuration with env vars
configure_environment()
