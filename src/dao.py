from db import db, User, FriendRequest


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

