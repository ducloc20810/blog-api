from flask import Blueprint
from main.engines.user import get_user_by_id
from main.schemas.user import UserResponseSchema
from main.schemas.post import PostResponseSchema
from main.libs.common import to_response

userController = Blueprint("user", __name__)


@userController.get("/users/<id>")
def get_user_with_id(id):
    user = get_user_by_id(id)

    if user is None:
        return {"message": "User not found"}, 404

    return {"user": to_response(schema=UserResponseSchema, clsObject=user)}, 200


@userController.get("/users/<id>/liked")
def get_user_liked_posts_by_id(id):
    user = get_user_by_id(id)

    if user is None:
        return {"message": "User not found"}, 404

    response = []
    for post in user.likes:
        response.append(to_response(schema=PostResponseSchema, clsObject=post))

    return {"total_item": len(response), "items": response}, 200


@userController.get("/users/<id>/read")
def get_user_liked_posts_by_id(id):
    user = get_user_by_id(id)

    if user is None:
        return {"message": "User not found"}, 404

    response = []
    for post in user.reads:
        response.append(to_response(schema=PostResponseSchema, clsObject=post))

    return {"total_item": len(response), "items": response}, 200


@userController.get("/users/<id>/favorites")
def get_user_liked_posts_by_id(id):
    user = get_user_by_id(id)

    if user is None:
        return {"message": "User not found"}, 404

    response = []
    for post in user.favorites:
        response.append(to_response(schema=PostResponseSchema, clsObject=post))

    return {"total_item": len(response), "items": response}, 200
