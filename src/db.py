import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, UniqueConstraint

db = SQLAlchemy()

friendships = db.Table('friends', db.Model.metadata,
                       db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                       db.Column('friend_id', db.Integer, db.ForeignKey('users.id')),
                       UniqueConstraint('user_id', 'friend_id', name='unique_friendships'))

user_groups = db.Table('user_groups', db.Model.metadata,
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('group_id', db.Integer, db.ForeignKey('groups.id')))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    friends = db.relationship('User', secondary=friendships,
                              primaryjoin=id == friendships.c.user_id,
                              secondaryjoin=id == friendships.c.friend_id)

    groups = db.relationship('Group', secondary=user_groups, back_populates='members')

    def direct_message_with(self, friend):
        for group in self.groups:
            if len(group.members) == 2 and friend in group.members:
                return group.id
            return None

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

    def serialize(self, extended=False):
        serialized = {
            'id': self.id,
            'username': self.username,
            'name': self.name
        }
        if extended:
            serialized['friends'] = [t.serialize() for t in self.friends]
            serialized['groups'] = [t.serialize() for t in self.groups]
        return serialized


class FriendRequest(db.Model):
    __tablename__ = 'friend requests'
    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    timestamp = db.Column(DateTime, default=datetime.datetime.utcnow())
    message = db.Column(db.String)

    def serialize(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'timetsamp': self.timestamp.__str__(),
            'message': self.message,
        }


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    direct_message = db.Column(db.Boolean, default=False)

    members = db.relationships('User', secondary=user_groups, back_populates='groups')

    messages = db.relationship('Message', cascade='delete')

    def serialize(self, extended=False):
        serialized = {
            'id': self.id,
            'name': self.name
        }
        if extended:
            serialized['members'] = [t.serialize() for t in self.members],
            serialized['messages'] = [t.serialize() for t in self.messages]

        return serialized


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

    timestamp = db.Column(DateTime, default=datetime.datetime.utcnow())

    message = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'group_id': self.group_id,
            'timestamp': self.timestamp.__str__(),
            'message': self.message,
        }
