import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, UniqueConstraint

db = SQLAlchemy()

friendships = db.Table('friends', db.Model.metadata,
                       db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                       db.Column('friend_id', db.Integer, db.ForeignKey('users.id')),
                       UniqueConstraint('user_id', 'friend_id', name='unique_friendships'))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    friends = db.relationship('User', secondary=friendships,
                              primaryjoin=id == friendships.c.user_id,
                              secondaryjoin=id == friendships.c.friend_id)

    def is_friend(self, friend):
        if friend in self.friends:
            return True
        else:
            return False

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            friend.friends.remove(self)

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

    def serialize(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'timetsamp': self.timestamp.__str__(),
            'message': self.message,
        }
