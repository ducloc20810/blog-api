from ..db import ma
from marshmallow import fields


class PostSchema(ma.Schema):
    title = fields.Str(required=True, allow_none=False)
    content = fields.Str(required=False, allow_none=True)
    author = fields.Str(required=True, allow_none=False)
    created_at = fields.DateTime(required=True, allow_none=False)
