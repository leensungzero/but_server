from app.view import BaseResource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.model.evaluation import PersonalityModel, AttentionModel, CharacterModel, IntroductionModel


class PersonalityView(BaseResource):
    @jwt_required
    def post(self):
        num = request.json['num']
        receiver = request.json['receiver']
        if PersonalityModel.get_personality(receiver) > 8:
            return '', 409

        PersonalityModel.post_personality(get_jwt_identity(), receiver, int(num))
        return '', 201


class AttentionView(BaseResource):
    @jwt_required
    def post(self):
        num = request.json['num']
        receiver = request.json['receiver']
        if AttentionModel.get_attention(receiver) > 8:
            return '', 409

        AttentionModel.post_attention(get_jwt_identity(), receiver, int(num))
        return '', 201


class CharacterView(BaseResource):
    @jwt_required
    def post(self):
        num = request.json['num']
        receiver = request.json['receiver']
        if CharacterModel.get_character(receiver) > 8:
            return '', 409

        CharacterModel.post_character(get_jwt_identity(), receiver, int(num))
        return '', 201


class IntroductionView(BaseResource):
    @jwt_required
    def post(self):
        content = request.json['content']
        receiver = request.json['receiver']
        if IntroductionModel.get_introduction(receiver):
            return '', 409

        IntroductionModel.post_introdution(get_jwt_identity(), receiver, content)
        return '', 201
