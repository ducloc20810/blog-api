from main.schemas.base import BaseSchema


class RoleSchema(BaseSchema):
    id: int
    name: str
