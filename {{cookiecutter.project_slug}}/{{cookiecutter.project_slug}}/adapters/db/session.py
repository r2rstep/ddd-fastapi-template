import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.project_slug}}.config import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

async_db = databases.Database(config.SQLALCHEMY_DATABASE_URI)
