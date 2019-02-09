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
                    break
            else:
                return fn(*args, **kwargs)
            raise BadRequestException()
        return wrapper
    return decorator


# Account
AUTH_POST_JSON = dict(id=str, password=str)
SIGNUP_POST_JSON = dict(name=str, id=str, password=str)
ADDITIONAL_POST_JSON = dict(id=str, gende=int, age=int, address=str, intro=str)
