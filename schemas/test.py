from ..db import ma


class TestSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
