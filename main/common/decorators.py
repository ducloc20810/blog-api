from functools import wraps
from typing import Type
from flask import request, g
import pydantic

from main.libs.token import decode_access_token
from ..engines.user import get_user_by_id
import datetime


def get_access_token() -> str | None:
    if "Authorization" in request.headers:
        return request.headers["Authorization"][len("Bearer ") :]

    if "Access-token" in request.headers:
        return request.headers["Access-token"]

    return None


def require_access_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = get_access_token()

        # Check token valid
        if token is None:
            return {"message": "Missing access token"}, 401

        token_payload = decode_access_token(token)

        time_zone = datetime.timezone.utc

        # Check token expired
        if datetime.datetime.now(time_zone) > token_payload.exp.replace(
            tzinfo=time_zone
        ):
            return {"message": "Token expired"}, 401

        # Check token's user_id
        user_id = token_payload.sub

        user = get_user_by_id(user_id)

        if user is None:
            return {"message": "Invalid token"}, 401

        g.user = user
        return f(*args, **kwargs)

    return wrapper


def get_request_args():
    if request.method == "GET":
        return request.args.to_dict()

    return request.get_json() or {}


def parse_args_with(schema: Type[pydantic.BaseModel]):
    def decorator(f):
        @wraps(f)
        def wrapper(**kwargs):
            request_args = get_request_args()
            parsed_args = schema.parse_obj(request_args)
            return f(**kwargs, args=parsed_args)

        return wrapper

    return decorator
