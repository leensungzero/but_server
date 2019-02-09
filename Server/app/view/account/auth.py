from datetime import timedelta
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flasgger import swag_from

from app.doc.auth import AUTH_POST
from app.view import BaseResource
from app.model import UserModel
from app.util.json_schema import json_type_validate, AUTH_POST_JSON


class AuthView(BaseResource):
    @json_type_validate(AUTH_POST_JSON)
    @swag_from(AUTH_POST)
    def post(self):
        student = UserModel.login(request.json['id'], request.json['password'])
        access_token = create_access_token(student.id, expires_delta=timedelta(days=2))
        refresh_token = create_refresh_token(student.id, expires_delta=timedelta(days=30))

        return {
            'accessToken': access_token,
            'refreshToken': refresh_token
        }
