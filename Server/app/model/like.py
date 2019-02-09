from app.extension import db
from app.model.mixin import BaseMixin
from app.model import UserModel


class LikeModel(db.Model, BaseMixin):
    __tablename__ = 'like'
    __table_args__ = (
        db.PrimaryKeyConstraint('sender', 'receiver'),
    )
    sender = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    receiver = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))

    def __init__(self, sender: str, receiver: str):
        self.sender = sender
        self.receiver = receiver

    @staticmethod
    def check_like_exist(my_id: str, others_id: str):
        return LikeModel.query.filter_by(sender=my_id, receiver=others_id).first()

    @staticmethod
    def get_like_from_others(id: str):
        return UserModel.query.filter_by(receiver=id).first()

    @staticmethod
    def get_like_i_sent(id: str):
        return LikeModel.query.filter_by(sender=id).all()

    @staticmethod
    def post_like(my_id: str, others_id: str):
        if LikeModel.check_like_exist(my_id, others_id):
            return '', 409

        LikeModel(my_id, others_id).save()

