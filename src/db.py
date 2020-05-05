import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

db = SQLAlchemy()

friends_association_table = db.Table('friends', db.Model.metadata,
                                     db.Column('user_1_id', db.Integer, db.ForeignKey('users.id')),
                                     db.Column('user_2_id', db.Integer, db.ForeignKey('users.id')))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    friends = db.relationship('User', secondary=friends_association_table, back_populates='friends')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name
        }


class FriendRequest(db.Model):
    __tablename__ = 'friend requests'
    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    timestamp = db.Column(DateTime, default=datetime.datetime.utcnow)
    message = db.Column(db.String)
    accepted = db.Column(db.Boolean)

    def serialize(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'timetsamp': self.timestamp,
            'message': self.message,
            'accepted': self.accepted
        }
