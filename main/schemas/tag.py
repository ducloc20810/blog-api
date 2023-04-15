from pydantic import BaseModel


class TagSchema(BaseModel):
    name: str
    created_at: str
