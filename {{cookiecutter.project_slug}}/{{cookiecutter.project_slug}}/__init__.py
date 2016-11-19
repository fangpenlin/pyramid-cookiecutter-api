from pyramid.config import Configurator

from .request import Request

__version__ = '0.0.0'


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application.

    """
    config = Configurator(
        request_factory=Request,
        settings=settings,
    )

    config.include('.models')
    config.include('.routes')
    config.include('.renderers')
    config.scan(categories=('pyramid', ))
    return config.make_wsgi_app()
