from typing import Type

import pydantic


def to_response(schema: Type[pydantic.BaseModel], clsObject):
    response_data = schema.from_orm(clsObject)
    return response_data.dict()
