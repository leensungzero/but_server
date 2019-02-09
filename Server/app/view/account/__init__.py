from flask import Blueprint
from flask_restful import Api

account_blueprint = Blueprint('account_blueprint', __name__)
account_api = Api(account_blueprint)

