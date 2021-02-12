from typing import Generator

from {{ cookiecutter.project_slug }}.adapters.db.session import Session


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()
