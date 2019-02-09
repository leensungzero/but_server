import bcrypt
from typing import Union

from app.extension import db
from app.exception import NoContentException, ResetContentException
from app.model.mixin import BaseMixin


class UserModel(db.Model, BaseMixin):
    __tablename__ = 'user'
    id = db.Column(db.String, primary_key=True)
    pw = db.Column(db.String)
    name = db.Column(db.String)
    gender = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String, nullable=True)
    intro = db.Column(db.String, nullable=True)

    def __init__(self, id: str, pw: str, name: str):
        self.id = id
        self.pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()).decode()
        self.name = name

    def additional(self, gender: int, age: int, address: str, intro: str):
        self.gender = gender
        self.age = age
        self.address = address
        self.intro = intro

    @staticmethod
    def get_user_by_id(id: str) -> 'UserModel':
        return UserModel.query.filter_by(id=id).first()

    @staticmethod
    def signup(name, id, pw):
        if UserModel.get_user_by_id(id) is not None:
            raise ResetContentException()

        UserModel(name, id, pw).save()

    @staticmethod
    def add_additional(id: str, gender: int, age: int, address: str, intro: str):
        user = UserModel.get_user_by_id(id)
        if user is None:
            raise ResetContentException()

        user.gender = gender
        user.age = age
        user.address = address
        user.intro = intro

        db.session.commit()

    @staticmethod
    def login(id: str, pw: str) -> Union[None, 'UserModel']:
        user: UserModel = UserModel.get_user_by_id(id)
        if not user or not bcrypt.checkpw(pw.encode('utf-8'), user.pw.encode('utf-8')):
            raise NoContentException()
        return user

