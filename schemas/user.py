from ..db import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    first_name = fields.Str(required=True, allow_none=False)
    middle_name = fields.Str(required=False, allow_none=True)
    last_name = fields.Str(required=True, allow_none=False)
    email = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)

class LoginSchema(ma.Schema):
    email = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)