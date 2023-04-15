from ..db import db
from ..models.user import User
from ..schemas.user import UserSchema


def create_user(data: UserSchema) -> User:
    new_user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        middle_name=data["middle_name"] if hasattr(data, "middle_name") else "",
        password=data["password"],
        email=data["email"],
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


def get_user_by_email(email: str) -> User:
    return User.query.filter(User.email == email).one_or_none()


def get_user_by_id(id: int) -> User:
    return User.query.filter(User.id == id).one_or_none()