import pytest
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.adapters import db as _db
from {{cookiecutter.project_slug}}.bootstrap import bootstrap


@pytest.fixture
def db() -> Session:
    bootstrap()
    yield _db.session.Session()
