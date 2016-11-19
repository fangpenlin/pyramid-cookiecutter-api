import contextlib
import os

import pytest
import transaction
from sqlalchemy.orm import scoped_session

from {{ cookiecutter.project_slug }} import models
from {{ cookiecutter.project_slug }}.database import tables


@pytest.fixture
def app_settings():
    db_url = os.environ.get(
        'TEST_DB', 'postgres://{{ cookiecutter.project_slug }}:{{ cookiecutter.project_slug }}@localhost/{{ cookiecutter.project_slug }}_test'
    )
    return {
        'sqlalchemy.url': db_url,
    }


@pytest.yield_fixture
def db_engine(app_settings):
    engine = models.get_engine(app_settings)
    if bool(os.environ.get('DB_ECHO', 0)):
        engine.echo = True
    return engine


@pytest.yield_fixture
def db_session_factory(db_engine):
    return models.get_session_factory(db_engine)


@pytest.yield_fixture
def db_transaction(db_engine, db_session_factory):
    tables.metadata.bind = db_engine
    tables.metadata.drop_all()
    tables.metadata.create_all()

    Session = scoped_session(db_session_factory)

    @contextlib.contextmanager
    def _db_transaction():
        with transaction.manager:
            yield models.get_tm_session(
                Session,
                transaction.manager,
                keep_session=True,
            )

    yield _db_transaction
    Session.close()
    Session.remove()
    db_engine.dispose()
