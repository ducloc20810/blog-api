from flask import Blueprint, request, g
from ..engines.user import get_user_by_id
from ..schemas.user import UserResponseSchema
from ..common.decorators import require_access_token

userController = Blueprint("user", __name__)
user_schema = UserResponseSchema()


@userController.get("/users/<id>")
def get_user_with_id(id):
    user = get_user_by_id(id)

    if user is not None:
        return {"data": user_schema.dump(user)}, 200

    return {"message": "User not found"}, 404


@userController.get("/me")
@require_access_token
def get_profile():
    user = g.user

    if user is None:
        return {"message": "User not found"}, 404

    return {"data": user_schema.dump(user)}, 200
