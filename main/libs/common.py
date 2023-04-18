from typing import Type
from main.schemas.base import BaseSchema
import pydantic
from typing import TypeVar

T = TypeVar("T")


def to_response(schema: Type[pydantic.BaseModel], clsObject):
    response_data = schema.from_orm(clsObject)
    return response_data.dict()


def update_schema_data(data: T, updateData: BaseSchema) -> T:
    for key, value in updateData.dict(exclude_unset=True).items():
        setattr(data, key, value)

    return data
