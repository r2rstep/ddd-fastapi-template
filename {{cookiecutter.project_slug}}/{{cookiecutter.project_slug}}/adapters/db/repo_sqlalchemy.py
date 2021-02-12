from typing import Any, Dict, Generic, Type, TypeVar, Union, cast

from fastapi.encoders import jsonable_encoder  # that's ugly to have API framework dependency in here
from fastapi_users.db import SQLAlchemyUserDatabase
from pydantic import BaseModel, UUID4
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from . import model_base, models, repository_base
from .session import async_db
from {{ cookiecutter.project_slug }} import domain

DomainModelType = TypeVar("DomainModelType", bound=BaseModel)
DbModelType = TypeVar("DbModelType", bound=model_base.Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class GenericSqlAlchemyRepo(repository_base.AbstractRepository,
                            Generic[DomainModelType, DbModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, db_model: Type[DbModelType], domain_model: Type[DomainModelType]):
        self.db_model = db_model
        self.domain_model = domain_model

    def get(self, db: Session, id: Any) -> (DbModelType, DomainModelType):
        db_obj = db.query(self.db_model).filter(self.db_model.id == id).first()
        return db_obj, self.domain_model.from_orm(db_obj)

    def add(self, db: Session, *, obj_in: CreateSchemaType) -> (DbModelType, DomainModelType):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.db_model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj, self.domain_model.from_orm(db_obj)

    def update(
            self,
            db: Session,
            *,
            db_obj: DbModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> (DbModelType, DomainModelType):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        columns = [col.key for col in inspect(db_obj).mapper.column_attrs]
        for field in update_data:
            if field in columns:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj, self.domain_model.from_orm(db_obj)

    def remove(self, db: Session, *, id: Any) -> (DbModelType, DomainModelType):
        db_obj = db.query(self.db_model).get(id)
        db.delete(db_obj)
        db.commit()
        return db_obj, self.domain_model.from_orm(db_obj)

    def remove_all(self, db: Session):
        for obj in db.query(self.db_model).all():
            db.delete(obj)
        db.commit()

    def count(self, db: Session) -> int:
        return db.query(self.db_model).count()


class User(repository_base.AbstractRepository):
    async def get(self, db: SQLAlchemyUserDatabase, id: UUID4) -> (models.UserDB, domain.User):
        db_obj = await db.get(id)
        return db_obj, domain.User.from_orm(db_obj)

    async def add(self, db: SQLAlchemyUserDatabase, *, user: domain.User) -> (models.UserDB, domain.User):
        db_obj = await db.create(cast(models.UserDB, user))
        return db_obj, domain.User.from_orm(db_obj)

    async def update(
            self,
            db: SQLAlchemyUserDatabase,
            *,
            user_db: models.UserDB,
            user: domain.User
    ) -> (DbModelType, DomainModelType):
        if isinstance(user, dict):
            update_data = user
        else:
            update_data = user.dict(exclude_unset=True)
        columns = [col.key for col in inspect(user_db).mapper.column_attrs]
        for field in update_data:
            if field in columns:
                setattr(user_db, field, update_data[field])
        await db.update(user_db)
        return user_db, domain.User.from_orm(user_db)

    async def remove(self, db: SQLAlchemyUserDatabase, *, user: domain.User) -> (models.UserDB, domain.User):
        await db.delete(cast(models.UserDB, user))
        return cast(models.UserDB, user), user

    async def remove_all(self, db: SQLAlchemyUserDatabase):
        raise NotImplemented

    async def count(self, db: Session) -> int:
        raise NotImplemented


{{ cookiecutter.aggregate_name_camel }} = GenericSqlAlchemyRepo[domain.{{ cookiecutter.aggregate_name_camel }},
                                      models.{{ cookiecutter.aggregate_name_camel }},
                                      domain.{{ cookiecutter.aggregate_name_camel }},
                                      domain.{{ cookiecutter.aggregate_name_camel }}]

{{ cookiecutter.aggregate_name_snake }} = {{ cookiecutter.aggregate_name_camel }}(models.{{ cookiecutter.aggregate_name_camel }}, domain.{{ cookiecutter.aggregate_name_camel }})

fastapi_user = SQLAlchemyUserDatabase(models.UserDB, async_db, models.User.__table__)

user = User()
