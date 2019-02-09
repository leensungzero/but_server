from flask import request, Response, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Api

from app.view import BaseResource
from app.model import UserModel, PersonalityModel, AttentionModel, CharacterModel
from app.util.json_schema import json_type_validate, SEARCH_BY_NAME_POST_JSON

personality_type = ['불친절함', '친절함', '보통', '최고', '인색함', '털털함', '말수가 적음', '수다스러움', '']
attention_type = ['먹을거리', '여행', '미용', '연애', '스포츠', '패션', '동물', '인테리어', '']
character_type = ['키가 큼', '키가 작음', '통통함', '마름', '염색함', '염색안함', '안경 씀', '안경안씀', '']

search_blueprint = Blueprint('search', __name__)
search_api = Api(search_blueprint)


class SearchByNameView(BaseResource):
    @jwt_required
    @json_type_validate(SEARCH_BY_NAME_POST_JSON)
    def get(self, name):
        user_list: list = UserModel.get_user_by_name(name)
        return [{
            'user_name': user.name,
            'user_id': user.id
        } for user in user_list], 200


class AllUserView(BaseResource):
    @jwt_required
    def get(self):
        user_list = UserModel.query.filter_by().all()

        personality = personality_type[PersonalityModel.get_personality(get_jwt_identity())]
        attention = attention_type[AttentionModel.get_attention(get_jwt_identity())]
        character = character_type[CharacterModel.get_character(get_jwt_identity())]

        return [{
            'user_name': user.name,
            'tag': [personality, attention, character],
        } for user in user_list], 200


search_api.add_resource(SearchByNameView, '/search/{name}')
search_api.add_resource(AllUserView, '/all')
