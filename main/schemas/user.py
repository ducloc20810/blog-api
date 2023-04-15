from main.schemas.base import BaseSchema


class UserSchema(BaseSchema):
    first_name: str
    middle_name: str | None
    last_name: str
    email: str
    password: bytes


class RegisterUserSchema(UserSchema):
    password: str


class UserResponseSchema(BaseSchema):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    email: str


class LoginSchema(BaseSchema):
    email: str
    password: str


class UpdateUserInfoSchema(BaseSchema):
    first_name: str | None
    middle_name: str | None
    last_name: str | None
