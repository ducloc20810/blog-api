from typing import List
from .base import BaseSchema
from .role import RoleSchema


class UserBasicSchema(BaseSchema):
    first_name: str
    middle_name: str | None
    last_name: str
    email: str


class UserSchema(UserBasicSchema):
    password: bytes


class RegisterUserRequestSchema(UserBasicSchema):
    roles: List[int]
    password: str


class UserResponseSchema(UserBasicSchema):
    id: int
    roles: List[RoleSchema]


class LoginSchema(BaseSchema):
    email: str
    password: str


class UpdateUserInfoSchema(BaseSchema):
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    roles: List[int] | None
