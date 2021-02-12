# FastAPI + PostgreSQL project template for DDD projects

The project provides template for DDD projects. It is heavily inspired by [Architecture patterns with Python](https://www.cosmicpython.com/)

## Project Generation

1. Use [cookiecutter](https://github.com/cookiecutter/cookiecutter) to generate project
2. Reformat code: `invoke sort-imports format`

## Outcome

After it is generated, the project:
* has authentication flow configured (register/login/reset password/refresh token) provided by [fastapi-users](https://github.com/frankie567/fastapi-users)
* has structure and basic classes for DDD following guideline in Architecture patterns with Python
* has backend, postgres and pgadmin services running
* environment is based on docker
