from flask import request, Blueprint, jsonify
from flask_restful import Api
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.view import BaseResource
from app.model import LikeModel


like_blueprint = Blueprint('like', __name__)
like_api = Api(like_blueprint)


class LikeView(BaseResource):
    @jwt_required
    def get(self):
        like_list = LikeModel.get_like_from_others(get_jwt_identity())
        return [{
            'user_id': user.id,
            'user_name': user.name
        } for user in like_list], 200

    @jwt_required
    def post(self):
        json = request.json

        LikeModel.post_like(get_jwt_identity(), json.get('receiver'))
        return '', 201


like_api.add_resource(LikeView, '/like')
