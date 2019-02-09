from flask import request
from flask_jwt_extended import jwt_required

from app.view import BaseResource
from app.model import UserModel


class MyPageView(BaseResource):
    @jwt_required
    def get(self):
        id = request.json['id']
        return UserModel.get_profile(id)
