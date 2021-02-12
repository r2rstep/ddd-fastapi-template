from fastapi_users import models
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer

from {{ cookiecutter.project_slug }} import domain
from .model_base import Base


class User(Base, SQLAlchemyBaseUserTable):
    pass


class UserDB(domain.User, models.BaseUserDB):
    class Config:
        orm_mode = True


class {{cookiecutter.aggregate_name_camel}}(Base):
    id = Column(Integer, primary_key=True)
    version_id = Column(Integer, nullable=False)
    prop = Column(Integer, nullable=False)

    __mapper_args__ = {
        "version_id_col": version_id
    }
