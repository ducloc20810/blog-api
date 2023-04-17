from flask import Blueprint, jsonify, request
from ..engines.user import get_user_by_id
from ..schemas.user import UserResponseSchema
from ..common.decorators import require_access_token
from ..libs.common import to_response

userController = Blueprint("user", __name__)


@userController.get("/users/<id>")
def get_user_with_id(id):
    user = get_user_by_id(id)

    if user is None:
        return {"message": "User not found"}, 404

    return {"user": to_response(schema=UserResponseSchema, clsObject=user)}, 200