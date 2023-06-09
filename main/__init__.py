from flask import Flask
from .controllers.home import home
from .controllers.auth import auth
from .controllers.user import userController
from .controllers.me import me
from .controllers.post import post
from .db import db


def create_db(app: Flask) -> None:
    with app.app_context():
        db.create_all()
        print("Database created successfully")


def add_routes(app: Flask) -> None:
    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(userController)
    app.register_blueprint(me)
    app.register_blueprint(post)


def create_app(config_file="config.py") -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    # init db and schema
    db.init_app(app)

    # routes
    add_routes(app)

    # Create database
    create_db(app)

    return app
