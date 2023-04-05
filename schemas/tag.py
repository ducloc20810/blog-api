from ..db import ma
from marshmallow import fields


class TagSchema(ma.Schema):
    name = fields.Str(required=True, allow_none=False)
    created_at = fields.DateTime(required=True, allow_none=False)
