from sqlalchemy.orm import Session

from db import db, User, FriendRequest, friendships


def get_all_users():
    return [t.serialize() for t in User.query.all()]


def create_user(username, name):
    new_user = User(
        username=username,
        name=name
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()


def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()


def delete_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None

    db.session.delete(user)
    db.session.commit()
    return user.serialize()


class AlreadyFriendsError(Exception):
    pass


def create_friend_request(sender_id, receiver_id, message):
    # check if they are already friends
    friendship_a = db.session.query(friendships).filter_by(user_1_id=sender_id, user_2_id=receiver_id).first()
    friendship_b = db.session.query(friendships).filter_by(user_1_id=receiver_id, user_2_id=sender_id).first()
    if friendship_a is not None or friendship_b is not None:
        raise AlreadyFriendsError

    # check if there is already an active request from the sender
    request_from_sender \
        = FriendRequest.query.filter_by(sender_id=sender_id, receiver_id=receiver_id).first()
    if request_from_sender is not None:
        return request_from_sender.serialize()

    # check if there is already an active request from the receiver
    request_from_receiver \
        = FriendRequest.query.filter_by(sender_id=receiver_id, receiver_id=sender_id).first()
    if request_from_receiver is not None and request_from_receiver.accepted is None:
        approve_friend_request(sender_id, request_from_receiver.id, True)
        return request_from_receiver.serialize()

    new_request = FriendRequest(
        sender_id=sender_id,
        receiver_id=receiver_id,
        message=message
    )

    db.session.add(new_request)
    db.session.comiit()
    return new_request.serialize()


def approve_friend_request(user_id, request_id, accepted):
    user = User.query.filter_by(id=user_id)
    if user is None:
        return None

    request = FriendRequest.query.filter_by(id=request_id, receiver_id=user_id)
    if request is None:
        return None

    if accepted:
        user.friends.append(request.sender_id)
    db.session.delete(request)
    db.commit()
    return request.serialize()


def get_all_friend_requests(user_id):
    return [t.serialize() for t in FriendRequest.query.filter_by(receiver_id=user_id).all()]


def get_all_friends(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [t.serialize() for t in user.friends]
