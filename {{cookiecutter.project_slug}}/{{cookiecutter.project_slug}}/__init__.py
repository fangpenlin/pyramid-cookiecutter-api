from pyramid.config import Configurator

from .request import Request
from .settings import default_settings

__version__ = '0.0.0'


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application.

    """
    app_settings = default_settings.copy()
    app_settings.update(settings)
    config = Configurator(
        request_factory=Request,
        settings=app_settings,
    )

    config.include('.models')
    config.include('.routes')
    config.include('.renderers')
    config.scan(categories=('pyramid', ))
    return config.make_wsgi_app()
