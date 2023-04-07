from flask import Flask
from .controllers.home import home
from .controllers.auth import register
from .db import db, ma


def create_db(app):
    with app.app_context():
        db.create_all()
        print("Database created successfully")


def add_routes(app):
    app.register_blueprint(home)
    app.register_blueprint(register)


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    # init db and schema
    db.init_app(app)
    ma.init_app(app)

    # routes
    add_routes(app)

    # Create database
    create_db(app)

    return app
