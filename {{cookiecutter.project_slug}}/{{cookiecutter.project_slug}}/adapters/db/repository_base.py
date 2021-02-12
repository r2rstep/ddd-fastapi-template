import abc
from typing import Any, Dict, TypeVar, Union

from pydantic import BaseModel

from . import model_base

DomainModelType = TypeVar("DomainModelType", bound=BaseModel)
DbModelType = TypeVar("DbModelType", bound=model_base.Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, db: Any, id: Any) -> (DbModelType, DomainModelType):
        pass

    @abc.abstractmethod
    def add(self, db: Any, *, obj_in: CreateSchemaType) -> (DbModelType, DomainModelType):
        pass

    @abc.abstractmethod
    def update(
            self,
            db: Any,
            *,
            db_obj: DbModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> (DbModelType, DomainModelType):
        pass

    @abc.abstractmethod
    def remove(self, db: Any, *, id: Any) -> (DbModelType, DomainModelType):
        pass

    @abc.abstractmethod
    def remove_all(self, db: Any):
        pass

    @abc.abstractmethod
    def count(self, db: Any) -> int:
        pass
