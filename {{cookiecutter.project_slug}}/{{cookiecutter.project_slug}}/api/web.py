from fastapi import FastAPI, Depends, status, APIRouter, Response
from sqlalchemy.orm import Session

from {{ cookiecutter.project_slug }} import bootstrap, service
from {{ cookiecutter.project_slug }}.adapters.db import session, models
from {{ cookiecutter.project_slug }}.domain.commands import Create{{ cookiecutter.aggregate_name_camel }}
from .deps import get_db
from . import users
from .resp_models import {{ cookiecutter.aggregate_name_camel }}Resp

app = FastAPI()

api_router = APIRouter()

{{ cookiecutter.aggregate_name_snake }}_router = APIRouter()
auth_router = APIRouter()


@app.on_event("startup")
async def on_startup():
    bootstrap.register_handlers()
    await session.async_db.connect()


@app.on_event("shutdown")
async def shutdown():
    await session.async_db.disconnect()


@{{ cookiecutter.aggregate_name_snake }}_router.post('', response_model={{ cookiecutter.aggregate_name_camel }}Resp, status_code=status.HTTP_201_CREATED)
async def create_{{ cookiecutter.aggregate_name_snake }}(cmd: Create{{ cookiecutter.aggregate_name_camel }},
                                                         db: Session = Depends(get_db),
                                                         _: models.UserDB = Depends(users.users.current_user())):
    aggreg = await service.create_aggreg(db, cmd)
    return {{ cookiecutter.aggregate_name_camel }}Resp(data=aggreg)


@auth_router.post('/refresh')
async def refresh_jwt(response: Response, user=Depends(users.users.current_user())):
    return await user.jwt_authentication.get_login_response(user, response)

auth_router.include_router(users.auth_router)
auth_router.include_router(users.register_router)
auth_router.include_router(users.reset_password_router)
auth_router.include_router(users.verify_router)

api_router.include_router({{ cookiecutter.aggregate_name_snake }}_router, prefix='/{{ cookiecutter.aggregate_name_snake }}s', tags=['{{ cookiecutter.aggregate_name_snake }}'])
api_router.include_router(auth_router, prefix='/auth', tags=['auth'])
api_router.include_router(users.users_router, prefix="/users", tags=["users"])
app.include_router(api_router, prefix='/api/v1')
