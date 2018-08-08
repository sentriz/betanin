import os
import click
import subprocess
from subprocess import Popen

from .config import Config


CLIENT_DIR = Config.CLIENT_DIR


@click.group()
def cli():
    sys.exit(1)


def _bash(cmd, **kwargs):
    click.echo('>s>> {}'.format(cmd))
    return subprocess.call(cmd, env=os.environ, shell=True, **kwargs)


@cli.command(help='server api dev server')
def serve_api():
    '''serve api dev server'''
    _bash('python run.py')


@cli.command(help='server client dev server')
def serve_client():
    '''serve client dev server'''
    _bash('npm run serve',
          cwd=CLIENT_DIR)


@cli.command(help='build client', name='build')
def build():
    '''build client'''
    _bash('npm run build',
          cwd=CLIENT_DIR)


if __name__ == '__main__':
    cli()
