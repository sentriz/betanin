import os
from glob import glob
from subprocess import call

import click
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.exceptions import NotFound


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


@click.command()
def test():
    """run the tests"""
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)


@click.command()
@click.option('-f', '--fix-imports', default=False, is_flag=True,
              help='Fix imports using isort, before linting')
def lint(fix_imports):
    """lint and check code style with flake8 and isort"""
    skip = ['requirements']
    root_files = glob('*.py')
    root_directories = [
        name for name in next(os.walk('.'))[1] if not name.startswith('.')]
    files_and_directories = [
        arg for arg in root_files + root_directories if arg not in skip]
    def execute_tool(description, *args):
        """execute a checking tool with it's arguments"""
        command_line = list(args) + files_and_directories
        click.echo('{}: {}'.format(description, ' '.join(command_line)))
        rv = call(command_line)
        if rv != 0:
            exit(rv)
    if fix_imports:
        execute_tool('fixing import order', 'isort', '-rc')
    execute_tool('checking code style', 'flake8')


@click.command()
def clean():
    """remove *.pyc and *.pyo files recursively starting at current directory"""
    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            if not (filename.endswith('.pyc') or filename.endswith('.pyo')):
                continue
            full_pathname = os.path.join(dirpath, filename)
            click.echo('Removing {}'.format(full_pathname))
            os.remove(full_pathname)
