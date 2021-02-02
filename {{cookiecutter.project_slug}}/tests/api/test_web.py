from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}} import domain


@pytest.mark.end2end
def test_create_aggreg(db: Session, client: TestClient):
    aggreg = client.post(f'/api/v1/{{cookiecutter.project_slug}}s', json=domain.commands.Create{{cookiecutter.aggregate_name_camel}}().dict())
    assert False
