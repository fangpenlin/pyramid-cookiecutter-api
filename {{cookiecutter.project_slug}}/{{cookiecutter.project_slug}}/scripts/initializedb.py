import click
import IPython

from . import subcommand
from .. import models


@subcommand
@click.command('initialize_db', short_help='initialize database')
@click.pass_context
def cli(ctx):
    settings = ctx.obj['settings']

    engine = models.get_engine(settings)
    tables.metadata.create_all(engine)

    with transaction.manager:
        dbsession = models.get_tm_session(
            models.get_session_factory(engine),
            transaction.manager,
        )
        # TODO: add seed data here
