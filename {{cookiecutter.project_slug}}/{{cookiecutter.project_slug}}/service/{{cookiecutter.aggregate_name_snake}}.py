from sqlalchemy.orm import Session


from {{ cookiecutter.project_slug }}.adapters.db import repo_sqlalchemy
from {{cookiecutter.project_slug}}.domain import {{cookiecutter.aggregate_name_snake}}, commands


async def create_aggreg(db: Session, command: commands.Create{{cookiecutter.aggregate_name_camel}}) -> {{cookiecutter.aggregate_name_snake}}.{{cookiecutter.aggregate_name_camel}}:
    logic = {{cookiecutter.aggregate_name_snake}}.{{cookiecutter.aggregate_name_camel}}Logic()
    created_{{ cookiecutter.aggregate_name_snake }} = logic.create(command.prop)
    _, {{ cookiecutter.aggregate_name_snake }}_db = repo_sqlalchemy.{{ cookiecutter.aggregate_name_snake }}.add(db, obj_in=created_{{ cookiecutter.aggregate_name_snake }})
    return {{ cookiecutter.aggregate_name_snake }}_db
