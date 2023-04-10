import datetime
import jwt
from .. import config
from pydantic import BaseModel


class JWTPayload(BaseModel):
    sub: int
    iat: datetime.datetime
    exp: datetime.datetime


def encode_access_token(user_id: int, lifetime=config.ACCESS_TOKEN_LIFE_TIME) -> str:
    iat = datetime.datetime.utcnow()
    payload = JWTPayload(
        sub=user_id,
        iat=iat,
        exp=iat + datetime.timedelta(seconds=lifetime),
    )

    return jwt.encode(payload.dict(), config.ACCESS_TOKEN_KEY, config.ALGORITHM)


def decode_access_token(access_token: str) -> JWTPayload:
    payload = jwt.decode(
        access_token, config.ACCESS_TOKEN_KEY, leeway=10, algorithms=[config.ALGORITHM]
    )

    return JWTPayload.parse_obj(payload)


def encode_refresh_token(user_id: int, lifetime=config.REFRESH_TOKEN_LIFE_TIME) -> str:
    iat = datetime.datetime.utcnow()
    payload = JWTPayload(
        sub=user_id,
        iat=iat,
        exp=iat + datetime.timedelta(seconds=lifetime),
    )

    return jwt.encode(payload.dict(), config.REFRESH_TOKEN_KEY, config.ALGORITHM)


def decode_refresh_token(refresh_token: str) -> JWTPayload:
    payload = jwt.decode(
        refresh_token,
        config.REFRESH_TOKEN_KEY,
        leeway=10,
        algorithms=[config.ALGORITHM],
    )

    return JWTPayload.parse_obj(payload)
