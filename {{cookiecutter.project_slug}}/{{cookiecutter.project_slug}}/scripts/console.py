import textwrap

import click
import IPython
from sqlalchemy.orm import scoped_session

from . import subcommand
from .. import models


@subcommand
@click.command('console', short_help='console')
@click.pass_context
def cli(ctx):
    settings = ctx.obj['settings']

    engine = models.get_engine(settings)
    session_factory = models.get_session_factory(engine)
    Session = scoped_session(session_factory)
    models.Base.query = Session.query_property()

    IPython.embed(
        header=textwrap.dedent('''\
        Local variables:
          Session - Database session
          models - Data models
        '''),
        local_ns={
            'Session': Session,
            'models': models,
        },
    )
