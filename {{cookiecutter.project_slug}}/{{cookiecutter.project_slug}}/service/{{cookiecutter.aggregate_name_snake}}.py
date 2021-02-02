from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.domain import {{cookiecutter.aggregate_name_snake}}, commands


async def create_aggreg(db: Session, command: commands.Create{{cookiecutter.aggregate_name_camel}}) -> {{cookiecutter.aggregate_name_snake}}.{{cookiecutter.aggregate_name_camel}}:
    logic = {{cookiecutter.aggregate_name_snake}}.{{cookiecutter.aggregate_name_camel}}Logic()
    return logic.create()
