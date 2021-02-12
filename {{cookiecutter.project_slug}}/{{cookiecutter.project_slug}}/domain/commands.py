from fastapi_users import models

from pydantic import BaseModel


class CreateUser(models.BaseUserCreate):
    pass


class UpdateUser(models.BaseUserUpdate):
    pass


class Create{{cookiecutter.aggregate_name_camel}}(BaseModel):
    prop: int
