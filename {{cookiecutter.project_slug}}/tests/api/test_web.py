from fastapi.testclient import TestClient
import pytest

from {{cookiecutter.project_slug}} import domain
from {{ cookiecutter.project_slug }}.adapters.db import models
from {{ cookiecutter.project_slug }}.api.resp_models import {{ cookiecutter.aggregate_name_camel }}Resp


@pytest.mark.end2end
def test_authenticated_user_can_create_{{ cookiecutter.aggregate_name_snake }}(client: TestClient, user: models.UserDB):
    login_resp = client.post('/api/v1/auth/login', data=dict(username=user.email, password='test'))
    assert login_resp.status_code == 200, str(login_resp.reason)
    token_data = login_resp.json()
    resp = client.post(f'/api/v1/{{ cookiecutter.aggregate_name_snake }}s',
                              headers=dict(Authorization=f'{token_data["token_type"]}'
                                                         f' {token_data["access_token"]}'),
                              json=domain.commands.Create{{ cookiecutter.aggregate_name_camel }}(prop=666).dict())
    assert resp.status_code == 201
    assert {{ cookiecutter.aggregate_name_camel }}Resp(**resp.json()).data.prop == 666


@pytest.mark.end2end
def test_nonauthenticated_user_cannot_create_aggregate(client: TestClient, user: models.UserDB):
    resp = client.post(f'/api/v1/{{ cookiecutter.aggregate_name_snake }}s',
                              json=domain.commands.Create{{ cookiecutter.aggregate_name_camel }}(prop=666).dict())
    assert resp.status_code == 401
