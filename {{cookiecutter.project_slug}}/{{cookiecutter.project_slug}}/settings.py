import os

env = os.environ

default_settings = {
    'sqlalchemy.url': env.get(
        'DATABASE_URL',
        '{{ cookiecutter.db_url }}',
    ),
}
