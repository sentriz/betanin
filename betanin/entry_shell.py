# standard library
import code

# 3rd party
import click

# betanin
from betanin import application


@click.command()
def main():
    'starts the betanin shell'
    app = application.create()
    with app.app_context():
        console = code.InteractiveConsole(locals=globals())
        console.interact(banner=f'''welcome to the betanin shell.
available globals include `Torrent`, `Line`, and `db`,
use `exit()` to exit.''')


if __name__ == '__main__':
    main()
