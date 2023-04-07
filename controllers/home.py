from flask import Blueprint

home = Blueprint("home", __name__)


@home.get("/")
def homepage():
    return "Hello World!"
