from typing import Generator

import asyncio
from fastapi.testclient import TestClient
import pytest

from {{ cookiecutter.project_slug }}.adapters.db import repo_sqlalchemy, models
from {{cookiecutter.project_slug}}.api.web import app
from .factories import UserFactory


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture
def user() -> models.UserDB:
    user = models.UserDB.from_orm(UserFactory.build())
    asyncio.get_event_loop().run_until_complete(repo_sqlalchemy.user.add(repo_sqlalchemy.fastapi_user,
                                                                         user=user))
    return user
