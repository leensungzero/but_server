from flask import Blueprint
from flask_restful import Api

evaluation_blueprint = Blueprint('evaluation', __name__)
evaluation_api = Api(evaluation_blueprint)

from .personality import PersonalityView
evaluation_api.add_resource(PersonalityView, '/personality')

