from pydantic import BaseModel

from {{cookiecutter.project_slug}} import domain


class {{cookiecutter.aggregate_name_camel}}Resp(BaseModel):
    class Links(BaseModel):
        self: str = None

    data: domain.{{cookiecutter.aggregate_name_camel}}Base
    links: Links = Links()
