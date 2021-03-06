from typing import Union

from app.extension import db
from app.exception import NoContentException, ResetContentException
from app.model.mixin import BaseMixin
from app.model.evaluation import CharacterModel, AttentionModel, PersonalityModel, IntroductionModel


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

    @staticmethod
    def get_profile(id: str):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            raise NoContentException()

        character_list = CharacterModel.get_character_list(id)
        personality_list = PersonalityModel.get_personality_list(id)
        attention_list = AttentionModel.get_attention_list(id)
        introduction_list = AttentionModel.get_attention_list(id)

        return {
            'userName': user.name,
            'userGender': user.gender,
            'userAge': user.age,
            'userIntro': user.intro,
            'character': character_list,
            'personality': personality_list,
            'attention': attention_list,
            'introduction': introduction_list
        }
