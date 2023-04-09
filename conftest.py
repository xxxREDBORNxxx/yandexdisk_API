import pytest
import requests
import configparser


@pytest.fixture(scope='session')
def config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope='session')
def session():
    return requests.Session()


@pytest.fixture(scope='session')
def yadisk_session(session, config):
    t = config['API']['token']
    if t:
        session.headers["Authorization"] = "OAuth " + t
    return session
