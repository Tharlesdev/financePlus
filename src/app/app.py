import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@click.command("init-db")
def init_db_command():
    db.create_all()
    click.echo("initialized the database")


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///financeplus.db",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    app.cli.add_command(init_db_command)

    return app
