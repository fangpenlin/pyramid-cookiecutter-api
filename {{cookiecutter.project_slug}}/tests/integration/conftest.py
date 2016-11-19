import contextlib
import os

import pytest
import transaction
import webtest
from sqlalchemy.orm import scoped_session

from {{ cookiecutter.project_slug }} import main
from {{ cookiecutter.project_slug }} import models
from {{ cookiecutter.project_slug }}.database import tables


@pytest.fixture
def testapp(app_settings):
    app = main({}, **app_settings)
    return webtest.TestApp(app)
