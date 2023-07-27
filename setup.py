# standard library
import os

# 3rd party
import setuptools


INFO = {
    "name": "betanin",
    "author": "Senan Kelly",
    "author_email": "senan@senan.xyz",
    "description": "beets based mitm of your torrent client and music player",
    "url": "https://github.com/sentriz/betanin",
}
ENTRY_POINTS = {
    "console_scripts": [
        "betanin = betanin.entry.betanin:main",
        "betanin-shell = betanin.entry.shell:main",
    ]
}
REQUIREMENTS = [
    "beets",
    "apprise",
    "alembic",
    "click",
    "Flask",
    "Flask-Cors",
    "Flask-JWT-Extended",
    "Flask-Migrate",
    "flask-restx",
    "Flask-SocketIO",
    "Flask-SQLAlchemy",
    "gevent",
    "pyxdg",
    "loguru",
    "ptyprocess",
    "python-engineio",
    "python-socketio",
    "SQLAlchemy",
    "SQLAlchemy-Utils",
    "toml",
]
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]


def get_version():
    with open("version.txt") as version_file:
        return f"v{version_file.read()}"


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


if __name__ == "__main__":
    version = get_version()
    print(f"setting up version {version}")
    setuptools.setup(
        **INFO,
        version=version,
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        install_requires=REQUIREMENTS,
        classifiers=CLASSIFIERS,
        entry_points=ENTRY_POINTS,
        include_package_data=True,
    )
