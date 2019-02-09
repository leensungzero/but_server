from app.extension import db
from app.model.mixin import BaseMixin

from enum import Enum


class PersonalityModel(db, BaseMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(20), primary_key=True)
    personality = db.Column(db.Integer)


class AttentionModel(db, BaseMixin):
    __tablename__ = 'attention'
    id = db.Column(db.String(20), primary_key=True)
    attention = db.Column(db.Integer)