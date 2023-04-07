from flask import Blueprint, request
import bcrypt
from ..schemas.user import UserSchema
from ..engines.user import create_user, get_user_by_email
from ..libs.access_token import encode, decode

user_schema = UserSchema()

register = Blueprint("register", __name__)


@register.post("/register")
def signup():
    data = request.get_json()
    password = data["password"].encode()
    data["password"] = bcrypt.hashpw(password, bcrypt.gensalt())

    errors = user_schema.validate(data)

    if errors:
        return {"message": "Validation errors", "errors": errors}, 400

    if get_user_by_email(data["email"]):
        return {"message": "User already existed"}, 400

    new_user = create_user(data)

    access_token = encode(new_user.id)
    return {"access_token": access_token}, 201
