from functools import wraps
from flask import request
from app.exception import BadRequestException


def json_type_validate(json_schema: dict):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for key, type_ in json_schema.items():
                value = request.json.get(key)
                if type(value) is not type_:
                    raise BadRequestException()
            else:
                return fn(*args, **kwargs)
        return wrapper
    return decorator
