from typing import List
from main.db import db
from main.models.user import User
from main.models.role import Role
from main.schemas.user import UpdateUserInfoSchema, UserSchema
from main.libs.common import update_schema_data


def create_user(data: UserSchema, roles: List[Role]) -> User:
    new_user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=data.password,
        roles=roles,
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


def get_user_by_email(email: str) -> User:
    return User.query.filter(User.email == email).one_or_none()


def get_user_by_id(id: int) -> User:
    return User.query.filter(User.id == id).one_or_none()


def update_user(
    user: User, data: UpdateUserInfoSchema, roles: List[Role]
) -> User | None:
    update_data = data.copy()
    update_data.roles = roles
    update_schema_data(data=user, update_data=update_data)

    db.session.commit()
    return user
