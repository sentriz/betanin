import os
import click
import subprocess
from subprocess import Popen

from .config import Config

CLIENT_DIR = Config.CLIENT_DIR


@click.group()
def cli():
    pass


def _bash(cmd, **kwargs):
    click.echo('>>> {}'.format(cmd))
    return subprocess.call(cmd, env=os.environ, shell=True, **kwargs)



@cli.command(help='server api dev server')
def serve_api():
    '''serve api dev server'''
    cmd = 'python run.py'
    _bash(cmd)


@cli.command(help='server client dev server')
def serve_client():
    '''serve client dev server'''
    cmd = 'npm run serve'
    _bash(cmd, cwd=CLIENT_DIR)


@cli.command(help='build client', name='build')
def build():
    '''build client'''
    cmd = 'npm run build'
    _bash(cmd, cwd=CLIENT_DIR)


if __name__ == '__main__':
    cli()
