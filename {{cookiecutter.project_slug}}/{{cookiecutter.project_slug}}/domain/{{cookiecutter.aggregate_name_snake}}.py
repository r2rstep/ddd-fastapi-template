from typing import List

import attr
from pydantic import BaseModel

from .event import Event


class {{cookiecutter.aggregate_name_camel}}Base(BaseModel):
    id: int = None


class {{cookiecutter.aggregate_name_camel}}({{cookiecutter.aggregate_name_camel}}Base):
    class Config:
        orm_mode = True


@attr.s(auto_attribs=True)
class {{cookiecutter.aggregate_name_camel}}Logic:
    events: List[Event] = attr.ib(factory=list)

    def create(self) -> {{cookiecutter.aggregate_name_camel}}:
        return {{cookiecutter.aggregate_name_camel}}Base()
