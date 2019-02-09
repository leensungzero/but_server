from flask import Flask
from flask_restful import Resource


class BaseResource(Resource):
    pass


class ExceptionController:
    """
    register_blueprint 시 defer되었던 함수들이 호출되며, flask-restful.Api._init_app()이 호출되는데
    해당 메소드가 app 객체의 에러 핸들러를 오버라이딩해서, 별도로 적용한 handler의 HTTPException 관련 로직이 동작하지 않음
    따라서 두 함수를 임시 저장해 두고, register_blueprint 이후 함수를 재할당하도록 함
    """

    def __init__(self, flask_app: Flask):
        self.app = flask_app
        self.handle_exception_func = None
        self.user_exception_func = None

    def __enter__(self):
        self.handle_exception_func = self.app.handle_exception
        self.handle_user_exception_func = self.app.handle_user_exception

    def __exit__(self, type, value, traceback):
        self.app.handle_exception = self.handle_exception_func
        self.app.handle_user_exception = self.handle_user_exception_func


def route(flask_app: Flask):
    with ExceptionController(flask_app):
        from .account import account_blueprint
        flask_app.register_blueprint(account_blueprint)
