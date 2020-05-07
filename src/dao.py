from sqlalchemy.orm import Session

from db import db, User, FriendRequest, friendships


def get_all_users():
    return [t.serialize() for t in User.query.all()]


def create_user(username, name):
    # check if there is already a user with that username
    same_username = User.query.filter_by(username=username).first()
    if same_username is not None:
        return None

    # if not, add the user
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


def create_friend_request(sender_id, receiver_id, message):
    if sender_id == receiver_id:
        return None

    sender = User.query.filter_by(id=sender_id).first()
    receiver = User.query.filter_by(id=receiver_id).first()
    if sender is None or receiver is None:
        return None

    # check if they are already friends
    if sender.is_friend(receiver):
        return None

    # check if there is already an active request from the sender
    request_from_sender \
        = FriendRequest.query.filter_by(sender_id=sender_id, receiver_id=receiver_id).first()
    if request_from_sender is not None:
        return request_from_sender.serialize()

    # check if there is already an active request from the receiver
    request_from_receiver \
        = FriendRequest.query.filter_by(sender_id=receiver_id, receiver_id=sender_id).first()
    if request_from_receiver is not None:
        return approve_friend_request(sender_id, request_from_receiver.id, True)

    new_request = FriendRequest(
        sender_id=sender_id,
        receiver_id=receiver_id,
        message=message
    )

    db.session.add(new_request)
    db.session.commit()
    return new_request.serialize()


def approve_friend_request(user_id, request_id, accepted):
    request = FriendRequest.query.filter_by(id=request_id, receiver_id=user_id).first()

    if request is None or user_id != request.receiver_id:
        return None

    if accepted:
        add_friend(user_id, request.sender_id)

    db.session.delete(request)
    db.session.commit()
    return request.serialize()


def get_all_friend_requests(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [t.serialize() for t in FriendRequest.query.filter_by(receiver_id=user_id).all()]


def add_friend(user_id, friend_id):
    user = User.query.filter_by(id=user_id).first()
    friend = User.query.filter_by(id=friend_id).first()
    if user is None or friend is None or user.is_friend(friend):
        return None
    user.add_friend(friend)
    return user.serialize()


def remove_friend(user_id, friend_id):
    user = User.query.filter_by(id=user_id).first()
    friend = User.query.filter_by(id=friend_id).first()
    if user is None or friend is None or not user.is_friend(friend):
        return None
    user.remove_friend(friend)
    return friend.serialize()


def get_all_friends(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [t.serialize() for t in user.friends]

