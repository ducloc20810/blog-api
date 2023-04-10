import datetime
from ..db import db
from ..models.refresh_token import RefreshToken
from ..libs.token import encode_refresh_token, decode_refresh_token


def get_refresh_token_by_user_id(user_id):
    return RefreshToken.query.filter(RefreshToken.user_id == user_id).one_or_none()


def check_refresh_token_expired(refresh_token):
    payload = decode_refresh_token(refresh_token)
    time_zone = datetime.timezone.utc
    return payload.exp.replace(tzinfo=time_zone) < datetime.datetime.now(time_zone)


def create_refresh_token(user_id):
    new_token = encode_refresh_token(user_id)

    new_refresh_token = RefreshToken(token=new_token, user_id=user_id)

    db.session.add(new_refresh_token)
    db.session.commit()

    return new_token


def delete_refresh_token(existing_refresh_token: RefreshToken) -> None:
    db.session.delete(existing_refresh_token)
    db.session.commit()
