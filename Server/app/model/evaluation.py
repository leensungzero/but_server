from app.extension import db
from app.model.mixin import BaseMixin


# 성격
class PersonalityModel(db.Model, BaseMixin):
    _tablename_ = 'personality'
    __table_args__ = (
        db.PrimaryKeyConstraint('id'),
    )
    id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    personality = db.Column(db.Integer)
    # 0: 불친절함, 1: 친절함, 2: 보통, 3: 최고, 4: 인색함, 5: 털털함, 6: 말수가 적음, 7: 수다스러움

    def __init__(self, id: str, personality: int):
        self.id = id
        self.personality = personality

    @staticmethod
    def get_personality_list(user_id: str):
        return PersonalityModel.query.filter_by(id=user_id).all()

    @staticmethod
    def get_personality(user_id: str):
        try:
            type_ = PersonalityModel.get_personality_list(user_id)[0].personality
            return type_
        except IndexError:
            return 8

    @staticmethod
    def post_personality(id: str, type_: int):
        PersonalityModel(id, type_).save()


# 관심사
class AttentionModel(db.Model, BaseMixin):
    _tablename_ = 'attention'
    __table_args__ = (
        db.PrimaryKeyConstraint('id',),
    )
    id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    attention = db.Column(db.Integer)
    # 0: 먹을거리, 1: 여행, 2: 미용, 3: 연애, 4: 스포츠, 5: 패션, 6: 동물, 7: 인테리어

    def __init__(self, id: str, personality: int):
        self.id = id
        self.personality = personality

    @staticmethod
    def get_attention_list(user_id: str):
        return AttentionModel.query.filter_by(id=user_id).all()

    @staticmethod
    def get_attention(user_id: str):
        try:
            type_ = AttentionModel.get_attention_list(user_id)[0].personality
            return type_
        except IndexError:
            return 8

    @staticmethod
    def post_attention(id: str, type_: int):
        PersonalityModel(id, type_).save()


# 특징
class CharacterModel(db.Model, BaseMixin):
    _tablename_ = 'character'
    __table_args__ = (
        db.PrimaryKeyConstraint('id',),
    )
    id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    character = db.Column(db.Integer)
    # 0: 키가 큼, 1: 키가 작음, 2: 통통함, 3: 마름, 4: 염색함, 5: 염색안함, 6: 안경 씀, 7: 안경안씀

    def __init__(self, id: str, personality: int):
        self.id = id
        self.personality = personality

    @staticmethod
    def get_character_list(user_id: str):
        return CharacterModel.query.filter_by(id=user_id).all()

    @staticmethod
    def get_character(user_id: str):
        try:
            type_ = CharacterModel.get_character_list(user_id)[0].personality
            return type_
        except IndexError:
            return 8

    @staticmethod
    def post_character(id: str, type_: int):
        CharacterModel(id, type_).save()


# 한 줄 소개
class IntroductionModel(db.Model, BaseMixin):
    __tablename__ = 'introduction'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', ),
    )
    id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    introduction = db.Column(db.String(50))

    def __init__(self, id: str, introdution: str):
        self.id = id
        self.introduction = introdution

    @staticmethod
    def get_introduction_list(user_id: str):
        return IntroductionModel.query.filter_by(id=user_id).all()