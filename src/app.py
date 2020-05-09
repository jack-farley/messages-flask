import json
from flask import Flask, request

import dao
from db import db

app = Flask(__name__)
db_filename = "messages.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename

db.init_app(app)
with app.app_context():
    db.create_all()


def success_response(data, code=200):
    return json.dumps({'success': True, 'data': data}), code


def failure_response(message, code=404):
    return json.dumps({'sucess': False, 'error': message}), code


@app.route('/api/users/', methods=['GET'])
def get_users():
    return success_response(dao.get_all_users())


@app.route('/api/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        username=body.get('username'),
        name=body.get('name')
    )
    if user is None:
        return failure_response("Username already exists.", 406)
    return success_response(user, 201)


@app.route('/api/users/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)


@app.route('/api/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user = dao.delete_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)


@app.route('/api/users/<int:user_id>/friends/requests/', methods=['POST'])
def send_friend_request(user_id):
    body = json.loads(request.data)
    friend_request = dao.create_friend_request(
        sender_id=user_id,
        receiver_id=body.get('receiver_id'),
        message=body.get('message')
    )
    if friend_request is None:
        return failure_response("Unable to create friend request.")
    return success_response(friend_request, 201)


@app.route('/api/users/<int:user_id>/friends/requests/', methods=['PUT'])
def approve_friend_request(user_id):
    body = json.loads(request.data)
    friend_request = dao.approve_friend_request(
        user_id=user_id,
        request_id=body.get('request_id'),
        accepted=body.get('accepted')
    )
    if friend_request is None:
        return failure_response("Unable to approve or deny friend request.")
    return success_response(friend_request)


@app.route('/api/users/<int:user_id>/friends/requests/', methods=['GET'])
def get_all_friend_requests(user_id):
    requests = dao.get_all_friend_requests(user_id)
    if requests is None:
        return failure_response("User not found.")
    return success_response(requests)


@app.route('/api/users/<int:user_id>/friends/', methods=['GET'])
def get_all_friends(user_id):
    friends = dao.get_all_friends(user_id)
    if friends is None:
        return failure_response("User not found.")
    return success_response(friends)


@app.route('/api/users/<int:user_id>/friends/', methods=['PUT'])
def remove_friend(user_id):
    body = json.loads(request.data)
    friend = dao.remove_friend(
        user_id=user_id,
        friend_id=body.get('friend_id')
    )
    if friend is None:
        return failure_response("Friend not found.")
    return success_response(friend)


@app.route('/api/groups/', methods=['POST'])
def create_group():
    body = json.loads(request.data)
    group = dao.create_group(
        creator_id=body.get('creator_id'),
        other_ids=body.get('other_user_ids'),
        name=body.get('name'),
    )
    if group is None:
        return failure_response("Creator not found.")
    return success_response(group, 201)


@app.route('/api/groups/<int:group_id>/', methods=['GET'])
def get_group_by_id(group_id):
    group = dao.get_group_by_id(group_id)
    if group is None:
        return failure_response("Group not found.")
    return success_response(group)


@app.route('/api/groups/<int:group_id>/', methods=['DELETE'])
def delete_group_by_id(group_id):
    group = dao.delete_group_by_id(group_id)
    if group is None:
        return failure_response("Group not found.")
    return success_response(group)


@app.route('/api/groups/members/', methods=['PUT'])
def add_user_to_group():
    body = json.loads(request.data)
    group_id = body.get('group_id')
    user_id = body.get('user_id')
    group = dao.add_user_to_group(user_id, group_id)
    if group is None:
        return failure_response("Unable to add user to group.")
    return success_response(group)


@app.route('/api/groups/members/remove/', methods=['PUT'])
def remove_user_from_group():
    body = json.loads(request.data)
    group_id = body.get('group_id')
    user_id = body.get('user_id')
    group = dao.remove_user_from_group(user_id, group_id)
    if group is None:
        return failure_response("Unable to remove user from group.")
    return success_response(group)


@app.route('/api/users/<int:user_id>/messages/group/', methods=['POST'])
def send_message_to_group(user_id):
    body = json.loads(request.data)
    group_id = body.get('group_id')
    text = body.get('message')
    message = dao.send_message_to_group(user_id, group_id, text)
    if message is None:
        return failure_response("Unable to send message.")
    return success_response(message)


@app.route('/api/users/<int:user_id>/messages/', methods=['POST'])
def send_message_to_user(user_id):
    body = json.loads(request.data)
    receiver_id = body.get('receiver_id')
    text = body.get('message')
    message = dao.send_message_to_user(user_id, receiver_id, text)
    if message is None:
        return failure_response("Unable to send message.")
    return success_response(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
