from typing import List
from flask import Blueprint
from main.common.decorators import parse_args_with, require_access_token
from main.engines.user import update_user
from main.libs.common import to_response
from main.schemas.user import UpdateUserInfoSchema, UserResponseSchema
from main.models.role import Role

me = Blueprint("me", __name__)


@me.get("/me")
@require_access_token
def get_profile(**kwargs):
    user = kwargs["user"]
    if user is None:
        return {"message": "User not found"}, 404

    return {"info": to_response(schema=UserResponseSchema, clsObject=user)}, 200


@me.put("/me")
@require_access_token
@parse_args_with(UpdateUserInfoSchema)
def update_profile(args: UpdateUserInfoSchema, **kwargs):
    user = kwargs["user"]

    roles: List[Role] = []

    for role_id in args.roles:
        role = Role.query.filter(Role.id == role_id).one_or_none()
        if role is None:
            raise f"Role id {role_id} not found"
        else:
            roles.append(role)

    updated_profile = update_user(user, args, roles)

    if updated_profile:
        return {
            "message": " Update profile successfully",
            "info": to_response(schema=UserResponseSchema, clsObject=updated_profile),
        }

    return {"message": "Update profile failed"}, 400
