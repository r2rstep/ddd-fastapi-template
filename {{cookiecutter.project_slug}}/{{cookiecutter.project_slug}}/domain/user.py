from fastapi_users import models


class User(models.BaseUser):
    class Config:
        orm_mode = True
