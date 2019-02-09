from flask import request, Response, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Api

from app.view import BaseResource
from app.model import UserModel, PersonalityModel
from app.util.json_schema import json_type_validate, SEARCH_BY_NAME_POST_JSON

type_ = ['불친절함', '친절함', '보통', '최고', '인색함', '털털함', '말수가 적음', '수다스러움']

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
        return [{
            'user_name': user.name,
            'tag': f'#{type_[PersonalityModel.get_personality(get_jwt_identity())]}'
        } for user in user_list], 200


search_api.add_resource(SearchByNameView, '/search/{name}')
search_api.add_resource(AllUserView, '/all')
