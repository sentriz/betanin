# standard library
import sys
import code

# 3rd party
import click

# betanin
from betanin import application
from betanin.models import Line  # noqa
from betanin.models import Torrent  # noqa
from betanin.extensions import DB  # noqa


WELCOME_MESSAGE = """\
|_  _ _|_ _  _ . _
|_)(/_ | (_|| ||| |
available variables include `Torrent`, `Line`, and `DB`
save your changes with `DB.session.commit()`
exit with `exit`\
"""


class Exit:
    """an instance of this naughty class assigned to `exit` allows
    you to type just `exit` to exit the repl - instead of `exit()`.
    you can call it as normal with parens too"""

    @staticmethod
    def __repr__():
        sys.exit()

    @staticmethod
    def __call__():
        sys.exit()


@click.command()
def main():
    "starts the betanin shell"
    app = application.create()
    with app.app_context():
        console = code.InteractiveConsole(
            locals={
                "Line": Line,
                "Torrent": Torrent,
                "app": app,
                "DB": DB,
                "exit": Exit(),
            }
        )
        console.interact(banner=WELCOME_MESSAGE)


if __name__ == "__main__":
    main()
