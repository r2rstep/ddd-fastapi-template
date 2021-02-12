from uuid import uuid4

import factory
from fastapi_users.password import get_password_hash

from {{ cookiecutter.project_slug }}.adapters.db import models


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.User

    id = factory.LazyAttribute(lambda _: uuid4())
    email = factory.Faker('email')
    hashed_password = factory.LazyAttribute(lambda obj: get_password_hash('test'))
    is_active = True
    is_verified = True
    is_superuser = False
