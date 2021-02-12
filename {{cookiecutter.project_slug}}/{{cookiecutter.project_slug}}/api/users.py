from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from {{ cookiecutter.project_slug }}.adapters.db import repo_sqlalchemy, models
from {{ cookiecutter.project_slug }}.config import config
from {{ cookiecutter.project_slug }} import domain


jwt_authentication = JWTAuthentication(
    secret=config.TOKEN_SECRET, lifetime_seconds=3600, tokenUrl=config.TOKEN_URL,
)


users = FastAPIUsers(
    repo_sqlalchemy.fastapi_user,
    [jwt_authentication],
    domain.User,
    domain.commands.CreateUser,
    domain.commands.UpdateUser,
    models.UserDB,
)


auth_router = users.get_auth_router(jwt_authentication)
register_router = users.get_register_router()
reset_password_router = users.get_reset_password_router(config.TOKEN_SECRET)
verify_router = users.get_verify_router(config.TOKEN_SECRET)
users_router = users.get_users_router()
