from app.view import BaseResource
from flask import request, jsonify

from app.model.evalutation import PersonalityModel


class PersonalityView(BaseResource):
    def get(self):
        personality_list = PersonalityModel.get_personality_list
        return jsonify([user for user in like_list]), 200