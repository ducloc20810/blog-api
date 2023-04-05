from flask import Blueprint
from ..models import user, post, tag, comment

home = Blueprint("home", __name__)


@home.get("/")
def homepage():
    return "Hello World!"
