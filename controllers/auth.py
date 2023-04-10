from flask import Blueprint, request
import bcrypt
from ..schemas.user import UserSchema, LoginSchema
from ..engines.user import create_user, get_user_by_email
from ..engines.refresh_token import (
    create_refresh_token,
    get_refresh_token_by_user_id,
    check_refresh_token_expired,
    delete_refresh_token,
)
from ..libs.token import encode_access_token, decode_access_token

user_schema = UserSchema()
login_schema = LoginSchema()

auth = Blueprint("auth", __name__)


@auth.post("/register")
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

    access_token = encode_access_token(new_user.id)

    refresh_token = create_refresh_token(new_user.id)

    return {"access_token": access_token, "refresh_token": refresh_token}, 201


@auth.post("/login")
def login():
    data = request.get_json()

    errors = login_schema.validate(data)
    if errors:
        return {"message": "Validation errors", "errors": errors}, 400

    user = get_user_by_email(data["email"])

    if user is None:
        return {"message": "User not found"}, 401

    if bcrypt.checkpw(data["password"].encode(), user.password) is False:
        return {"message": "Password does not match"}, 401

    access_token = encode_access_token(user.id)

    refresh_token = ""

    # Check if refresh token for user is created
    existing_token_object = get_refresh_token_by_user_id(user.id)

    # Check if existing token is expired or not
    if existing_token_object:
        token_string = existing_token_object.token
        # If token is expired, delete token
        if check_refresh_token_expired(token_string):
            delete_refresh_token(existing_token_object)
            refresh_token = create_refresh_token(user.id)
        else:
            refresh_token = existing_token_object.token
    else:
        refresh_token = create_refresh_token(user.id)

    return {"access_token": access_token, "refresh_token": refresh_token}, 201
