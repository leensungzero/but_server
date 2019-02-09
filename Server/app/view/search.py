from flask import request, Response, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Api

from app.view import BaseResource
from app.model import UserModel
from app.util.json_schema import json_type_validate, SEARCH_BY_NAME_POST_JSON


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
            'user_name': user.name
        } for user in user_list], 200


search_api.add_resource(SearchByNameView, '/search/{name}')
search_api.add_resource(AllUserView, '/all')
