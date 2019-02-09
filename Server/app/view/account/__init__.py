from flask import Blueprint
from flask_restful import Api

account_blueprint = Blueprint('account', __name__, url_prefix='/apply')
account_api = Api(account_blueprint)

from .auth import AuthView
account_api.add_resource(AuthView, '/auth')

from .signup import SignupView, AdditionalView
account_api.add_resource(SignupView, '/signup')
account_api.add_resource(AdditionalView, '/additional')
