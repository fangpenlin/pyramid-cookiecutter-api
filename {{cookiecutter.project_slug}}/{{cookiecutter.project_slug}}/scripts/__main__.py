import functools
import logging
import os
import sys
from logging.config import fileConfig

import click
import venusian
from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }} import scripts


LOG_MAPPING = {
    'd': logging.DEBUG,
    'debug': logging.DEBUG,
    'i': logging.INFO,
    'info': logging.INFO,
    'w': logging.WARNING,
    'warn': logging.WARNING,
    'e': logging.ERROR,
    'err': logging.ERROR,
    'error': logging.ERROR,
}

DEFAULT_CONFIG_FILE = '/etc/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.ini'

SCRIPTS_FOLDER = os.path.dirname(__file__)


class MasterCLI(click.MultiCommand):

    def __init__(self, *args, **kwargs):
        super(MasterCLI, self).__init__(*args, **kwargs)
        self.subcommands = self._scan_subcommands()

    def _scan_subcommands(self):
        subcommands = {}
        scanner = venusian.Scanner(subcommands=subcommands)
        scanner.scan(scripts, categories=('subcommands', ))
        return subcommands

    def list_commands(self, ctx):
        command_names = list(self.subcommands.keys())
        command_names.sort()
        return command_names

    def get_command(self, ctx, name):
        if name not in self.subcommands:
            return
        return self.subcommands[name]


@click.command(cls=MasterCLI, invoke_without_command=True)
@click.option(
    '-l', '--log-level',
    type=click.Choice(LOG_MAPPING.keys()),
    help='log LEVEL',
    default='info',
)
@click.option(
    '-c', '--conf-file',
    type=str,
    help='configuration FILE, defaults to {{ cookiecutter.project_slug | upper }}_CONF, use - for defaults',
    default=os.getenv('{{ cookiecutter.project_slug | upper }}_CONF', DEFAULT_CONFIG_FILE),
)
@click.option(
    '-v', '--version',
    is_flag=True,
    help='print {{ cookiecutter.project_slug }} version',
)
@click.pass_context
def cli(ctx, log_level, conf_file, version):
    click.echo('Log level: {}'.format(log_level), err=True)
    if os.path.exists(conf_file):
        click.echo('Configuration: {}'.format(conf_file), err=True)
        setup_logging(
            conf_file,
            fileConfig=functools.partial(
                fileConfig,
                disable_existing_loggers=False,
            ),
        )
    else:
        logging.basicConfig(level=LOG_MAPPING[log_level])
    settings = {}
    if os.path.exists(conf_file):
        cfg_settings = get_appsettings(conf_file, name='main')
        settings.update(cfg_settings)

    ctx.obj['log_level'] = log_level
    ctx.obj['conf_file'] = conf_file
    ctx.obj['settings'] = settings

    if version:
        click.echo({{ cookiecutter.project_slug }}.__version__)
        return
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help(), err=True)
        sys.exit(-1)


def main():
    cli(obj={})


if __name__ == '__main__':
    main()
