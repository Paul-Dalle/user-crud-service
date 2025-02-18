from flask import Blueprint, request, jsonify
from models import db, User
from db_utils import add_to_session, get_all_users, get_user_by_id, delete_user, update_user

user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], age=data['age'])
    added_user = add_to_session(new_user)

    return jsonify({"message": "User created", "id": added_user.id}), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email, "age": u.age} for u in users])


@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = get_user_by_id(id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email, "age": user.age})

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user_route(id):
    data = request.get_json()
    user = get_user_by_id(id)

    updated_user = update_user(user, data['name'], data['email'], data['age'])

    return jsonify({"message": "User updated", "id": updated_user.id})

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    user = get_user_by_id(id)

    delete_user(user)

    return jsonify({"message": "User deleted"})
