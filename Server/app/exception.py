from werkzeug.exceptions import HTTPException


class BaseException(HTTPException):
    pass


class NoContentException(BaseException):
    code = 204
    description = 'No Content'


class ResetContentException(BaseException):
    code = 205
    description = 'Reset Content'


class BadRequestException(BaseException):
    code = 400
    description = 'Bad Request'


class WrongAuthException(BaseException):
    code = 401
    description = 'Wrong Auth'
