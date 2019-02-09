from app.view import BaseResource
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.model.evaluation import PersonalityModel, AttentionModel, CharacterModel, IntroductionModel


class PersonalityView(BaseResource):
    def get(self):
        personality_list = PersonalityModel.get_personality_list
        return jsonify([personality for personality in personality_list]), 200


class AttentionView(BaseResource):
    def get(self):
        attention_list = AttentionModel.get_attention_list
        return jsonify([attention for attention in attention_list]), 200


class CharacterView(BaseResource):
    def get(self):
        character_list = CharacterModel.get_character_list
        return jsonify([character for character in character_list]), 200


class IntroductionView(BaseResource):
    def get(self):
        introduction_list = IntroductionModel.get_introduction_list
        return jsonify([introduction for introduction in introduction_list]), 200

    @jwt_required
    def post(self, type):
        PersonalityModel.post_personality(get_jwt_identity(), type)

        return '', 201