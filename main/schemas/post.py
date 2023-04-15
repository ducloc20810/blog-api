import datetime
from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
    author: str
    created_at: datetime.datetime
