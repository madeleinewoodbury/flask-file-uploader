from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

class Image(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    url = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.Column(db.String(50), db.ForeignKey('user.id'))
    description = db.Column(db.String(150))