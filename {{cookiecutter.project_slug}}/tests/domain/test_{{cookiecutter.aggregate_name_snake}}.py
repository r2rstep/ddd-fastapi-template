from {{cookiecutter.project_slug}}.domain.{{cookiecutter.aggregate_name_snake}} import {{cookiecutter.aggregate_name_camel}}Logic, {{ cookiecutter.aggregate_name_camel }}


def test_create_{{ cookiecutter.aggregate_name_snake }}():
    assert {{cookiecutter.aggregate_name_camel}}(prop=1) == {{ cookiecutter.aggregate_name_camel }}Logic().create(1)
