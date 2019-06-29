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
        "betanin = betanin.entry_betanin:main",
        "betanin-shell = betanin.entry_shell:main",
    ]
}
REQUIREMENTS = [
    "Click>=7.0",
    "Flask-Cors>=3.0.6",
    "Flask-Migrate>=2.3.0",
    "Flask-SQLAlchemy>=2.3.2",
    "Flask-SocketIO>=3.0.2",
    "Flask>=1.0.2",
    "ItsDangerous",
    "Jinja2>=2.10",
    "Mako>=1.0.7",
    "MarkupSafe>=1.0",
    "SQLAlchemy-Utils>=0.33.6",
    "SQLAlchemy>=1.2.12",
    "Werkzeug>=0.14.1",
    "alembic>=1.0.1",
    "aniso8601>=3.0.2",
    "apprise>=0.7.5",
    "beets==1.4.9",
    "certifi>=2018.10.15",
    "chardet>=3.0.4",
    "flask-jwt-extended",
    "flask-restplus>=0.12.1",
    "gevent>=1.3.7",
    "greenlet>=0.4.15",
    "idna>=2.7",
    "jsonschema>=2.6.0",
    "loguru",
    "ptyprocess",
    "python-dateutil>=2.7.3",
    "python-editor>=1.0.3",
    "python-engineio>=2.3.2",
    "python-socketio>=2.0.0",
    "pytz>=2018.5",
    "pyxdg>=0.26",
    "requests>=2.20.0",
    "six>=1.11.0",
    "sqlalchemy-json>=0.2.2",
    "toml",
    "tzlocal>=1.5.1",
    "urllib3>=1.24",
]
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]


def get_new_version():
    """gets the bumped version from the environment variable
    passed by the `tag-and-deploy` script in the project root"""
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
