from typing import Union

from app.extension import db
from app.exception import NoContentException, ResetContentException
from app.model.mixin import BaseMixin


class UserModel(db.Model, BaseMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(20), primary_key=True)
    pw = db.Column(db.String(100))
    name = db.Column(db.String(20))
    gender = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(200), nullable=True)
    intro = db.Column(db.String(200), nullable=True)

    def __init__(self, name: str, id: str, pw: str):
        self.id = id
        self.pw = pw
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
    def get_user_by_name(name: str):
        return UserModel.query.filter_by(name=name).all()

    @staticmethod
    def signup(name, id, pw):
        if UserModel.get_user_by_id(id) is not None:
            raise ResetContentException()

        UserModel(name, id, pw).save()

    @staticmethod
    def add_additional(id: str, gender: int, age: int, address: str, intro: str):
        user = UserModel.get_user_by_id(id)
        if user is None:
            raise NoContentException()

        user.gender = gender
        user.age = age
        user.address = address
        user.intro = intro

        db.session.commit()

    @staticmethod
    def login(id: str, pw: str) -> Union[None, 'UserModel']:
        user: UserModel = UserModel.get_user_by_id(id)
        if not user or pw != user.pw:
            raise NoContentException()
        return user

