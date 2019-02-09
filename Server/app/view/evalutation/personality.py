from app.view import BaseResource
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.model.evalutation import PersonalityModel


class PersonalityView(BaseResource):
    @jwt_required
    def post(self, type):
        PersonalityModel.post_personality(get_jwt_identity(), type)

        return '', 201
