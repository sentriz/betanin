import os
from glob import glob
from subprocess import call

import click


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


@click.command()
def test():
    'Runs the tests.'
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)


@click.command()
def clean():
    'Removes *.pyc and *.pyo files recursively starting at current directory.'
    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            if not (
                filename.endswith('.pyc')
                or filename.endswith('.pyo')
            ):
                continue
            full_pathname = os.path.join(dirpath, filename)
            click.echo(f'removing {full_pathname}')
            os.remove(full_pathname)
