from sqlalchemy import Column, Integer

from .model_base import Base


class {{cookiecutter.aggregate_name_camel}}(Base):
    id = Column(Integer, primary_key=True)
    version_id = Column(Integer, nullable=False)

    __mapper_args__ = {
        "version_id_col": version_id
    }
