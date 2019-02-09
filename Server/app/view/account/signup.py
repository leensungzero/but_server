from flask import request, Response
from flasgger import swag_from

from app.doc.signup import SIGNUP_POST, ADDITIONAL_PATCH
from app.view import BaseResource
from app.model import UserModel
from app.util.json_schema import json_type_validate, SIGNUP_POST_JSON, ADDITIONAL_POST_JSON


class SignupView(BaseResource):
    @json_type_validate(SIGNUP_POST_JSON)
    @swag_from(SIGNUP_POST)
    def post(self):
        name = request.json['name']
        id = request.json['id']
        pw = request.json['password']

        UserModel.signup(name, id, pw)

        return Response('', 201)


class AdditionalView(BaseResource):
    @json_type_validate(ADDITIONAL_POST_JSON)
    @swag_from(ADDITIONAL_PATCH)
    def patch(self):
        json = request.json

        UserModel.add_additional(
            id=json['id'],
            gender=json['gender'],
            age=json['age'],
            address=json['address'],
            intro=json['intro']
        )

        return Response('', 201)
