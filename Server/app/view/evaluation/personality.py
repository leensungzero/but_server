from app.view import BaseResource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.model.evaluation import PersonalityModel, AttentionModel, CharacterModel, IntroductionModel


class PersonalityView(BaseResource):
    @jwt_required
    def post(self):
        num = request.json['num']
        if PersonalityModel.get_personality(get_jwt_identity()) != 8:
            return '', 409

        PersonalityModel.post_personality(get_jwt_identity(), int(num))
        return '', 201


class AttentionView(BaseResource):
    @jwt_required
    def post(self):
        num = request.json['num']
        if AttentionModel.get_attention(get_jwt_identity()) != 8:
            return '', 409

        AttentionModel.post_attention(get_jwt_identity(), int(num))
        return '', 201


class CharacterView(BaseResource):
    @jwt_required
    def post(self):
        num = request.json['num']
        if CharacterModel.get_character(get_jwt_identity()) != 8:
            return '', 409

        CharacterModel.post_character(get_jwt_identity(), int(num))
        return '', 201


class IntroductionView(BaseResource):
    @jwt_required
    def post(self):
        content = request.json['content']
        if IntroductionModel.get_introduction(get_jwt_identity()):
            return '', 409

        IntroductionModel.post_introdution(get_jwt_identity(), content)
        return '', 201
