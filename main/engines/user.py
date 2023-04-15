from ..db import db
from ..models.user import User
from ..schemas.user import UpdateUserInfoSchema, UserSchema


def create_user(data: UserSchema) -> User:
    new_user = User(**data.__dict__)

    db.session.add(new_user)
    db.session.commit()

    return new_user


def get_user_by_email(email: str) -> User:
    return User.query.filter(User.email == email).one_or_none()


def get_user_by_id(id: int) -> User:
    return User.query.filter(User.id == id).one_or_none()


def update_user(id: int, data: UpdateUserInfoSchema) -> User | None:
    user = get_user_by_id(id)

    if user is None:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.session.commit()
    return user
