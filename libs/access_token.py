import datetime
import jwt
from .. import config
from pydantic import BaseModel


class JWTPayload(BaseModel):
    sub: int
    iat: datetime.datetime
    exp: datetime.datetime


def encode(user_id: int, lifetime=config.JWT_LIFETIME_IN_SECONDS) -> str:
    iat = datetime.datetime.utcnow()
    payload = JWTPayload(
        sub=user_id,
        iat=iat,
        exp=iat + datetime.timedelta(seconds=lifetime),
    )

    return jwt.encode(payload.dict(), config.SECRET_KEY, config.ALGORITHM)


def decode(access_token: str) -> JWTPayload:
    payload = jwt.decode(
        access_token, config.SECRET_KEY, leeway=10, algorithms=[config.ALGORITHM]
    )

    return JWTPayload.parse_obj(payload)
