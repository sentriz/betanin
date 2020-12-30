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
    "alembic==1.4.3",
    "aniso8601==8.1.0",
    "attrs==20.3.0",
    "bidict==0.21.2",
    "certifi==2020.12.5",
    "chardet==4.0.0",
    "click==7.1.2",
    "Flask==1.1.2",
    "Flask-Cors==3.0.9",
    "Flask-JWT-Extended==3.25.0",
    "Flask-Migrate==2.5.3",
    "flask-restplus==0.13.0",
    "Flask-SocketIO==4.3.2",
    "Flask-SQLAlchemy==2.4.4",
    "gevent==1.3.7",
    "greenlet==0.4.15",
    "idna==2.10",
    "importlib-metadata==3.3.0",
    "itsdangerous==1.1.0",
    "jellyfish==0.8.2",
    "Jinja2==2.11.2",
    "jsonschema==3.2.0",
    "loguru==0.5.3",
    "Mako==1.1.3",
    "MarkupSafe==1.1.1",
    "munkres==1.1.4",
    "musicbrainzngs==0.7.1",
    "mutagen==1.45.1",
    "ptyprocess==0.7.0",
    "PyJWT==1.7.1",
    "pyrsistent==0.17.3",
    "python-dateutil==2.8.1",
    "python-editor==1.0.4",
    "python-engineio==3.14.2",
    "python-socketio==4.6.1",
    "pytz==2020.5",
    "pyxdg==0.27",
    "PyYAML==5.3.1",
    "requests==2.25.1",
    "six==1.15.0",
    "SQLAlchemy==1.3.22",
    "sqlalchemy-json==0.4.0",
    "SQLAlchemy-Utils==0.36.8",
    "toml==0.10.2",
    "typing-extensions==3.7.4.3",
    "tzlocal==2.1",
    "Unidecode==1.1.2",
    "urllib3==1.26.2",
    "Werkzeug==0.16.1",
    "zipp==3.4.0",
    "zope.event==4.5.0",
    "zope.interface==5.2.0",
]
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]


def get_new_version():
    """gets the bumped version from the environment variable
    passed by the `_do_tag_and_deploy` script in the project root"""
    return os.getenv("NEW_VERSION", "development")


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


if __name__ == "__main__":
    new_version = get_new_version()
    print(f"setting up version {new_version}")
    setuptools.setup(
        **INFO,
        version=new_version,
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        install_requires=REQUIREMENTS,
        classifiers=CLASSIFIERS,
        entry_points=ENTRY_POINTS,
        include_package_data=True,
    )
