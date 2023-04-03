from flask import Blueprint
from ..models import user, like, post, post_tag, tag, comment, like, read, favorite

home = Blueprint("home", __name__)


@home.get("/")
def homepage():
    return "Hello World!"
