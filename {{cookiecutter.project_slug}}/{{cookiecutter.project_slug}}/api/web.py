from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}} import bootstrap
from {{cookiecutter.project_slug}}.domain.commands import Create{{cookiecutter.aggregate_name_camel}}
from {{cookiecutter.project_slug}} import service
from .deps import get_db
from .resp_models import {{cookiecutter.aggregate_name_camel}}Resp

app = FastAPI()


@app.on_event("startup")
def on_startup():
    bootstrap.register_handlers()


@app.post('/api/v1/{{cookiecutter.project_slug}}s',
          response_model={{cookiecutter.aggregate_name_camel}}Resp,
          status_code=status.HTTP_201_CREATED)
async def create_aggreg(cmd: Create{{cookiecutter.aggregate_name_camel}}, db: Session = Depends(get_db)):
    aggreg = await service.create_aggreg(db, cmd)
    return {{cookiecutter.aggregate_name_camel}}Resp(data=aggreg)
