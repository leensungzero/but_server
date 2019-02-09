from flask import Blueprint
from flask_restful import Api

evaluation_blueprint = Blueprint('evaluation', __name__)
evaluation_api = Api(evaluation_blueprint)

from .personality import PersonalityView, AttentionView, CharacterView, IntroductionView
evaluation_api.add_resource(PersonalityView, '/personality')
evaluation_api.add_resource(AttentionView, '/attention')
evaluation_api.add_resource(CharacterView, '/character')
evaluation_api.add_resource(IntroductionView, '/introdution')

