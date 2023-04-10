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
    existing_token_object = get_refresh_token_by_user_id(user_id)

    if existing_token_object:
        token_string = existing_token_object.token;
        if check_refresh_token_expired(token_string):
            db.session.delete(existing_token_object)
            db.session.commit()
        else:
            return token_string

    new_token = token = encode_refresh_token(user_id)

    new_refresh_token = RefreshToken(token=new_token, user_id=user_id)

    db.session.add(new_refresh_token)
    db.session.commit()

    return new_token
