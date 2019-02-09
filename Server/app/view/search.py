from flask import request, Response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.view import BaseResource
from app.model import UserModel
from app.util.json_schema import json_type_validate, SIGNUP_POST_JSON, ADDITIONAL_POST_JSON


class SearchByNameView(BaseResource):
    @jwt_required
    @json_type_validate(SEARCH_BY_NAME_POST_JSON)
    def post(self):
        user_list: list = UserModel.get_user_by_name(request.json.get('name'))
        return jsonify([user for user in user_list]), 200


class AllUserView(BaseResource):
    @jwt_required
    def get(self):
        user_list = UserModel.query.filter_by().all()
        return jsonify([user for user in user_list]), 200
