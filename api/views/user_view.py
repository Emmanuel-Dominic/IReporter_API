
"""views file for users, login, signup and logout sessions"""

from flask import Blueprint, jsonify, request, Response, json
from models.user_model import User,users_table
from helpers.auth import encode_token, admin_required,token_required
from helpers.validators import verify_login_data, verify_signup_data


from functools import wraps



user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1')


@user_bp.route('/users', methods=['GET'])
@token_required
@admin_required
def get_users():
    """docstring function that return all users detials"""
    users_list = []
    for user in users_table[1:]:
        users_list.append(user.get_user_details())
    return jsonify({
        "status": 200,
        "users": users_list
    }), 200


@user_bp.route('/auth/signup', methods=['POST'])
@verify_signup_data
def sign_up():
    data = request.get_json()
    name = {"firstName": data['firstName'], "lastName": data['lastName'], \
            "otherName": data['otherName']}
    email = data['email']
    phoneNumber = data['phoneNumber']
    password = data['password']
    userName = data['userName']

    for user in users_table:
        if email == user.email:
            return jsonify({"message": "sorry, Email already in use"}), 406
    new_user = User(userName=userName, \
                    name=name, email=email, \
                    phoneNumber=phoneNumber, \
                    password=password \
                    )
    users_table.append(new_user)
    return jsonify({"status": 201, "message": "Successfully registered", "users": new_user.get_user_details()}), 201


@user_bp.route('/auth/login', methods=['POST'])
@verify_login_data
def login():
    data = request.get_json()
    data['password']
    data['email']

    for user_obj in users_table:
        if data['email'] == user_obj.email and data['password'] == user_obj.password:
            return jsonify({"Token": encode_token(user_obj.userId), "message": "Successfully logged In"})

    return jsonify({"message": "Invalid credentials, Please try again"}), 401
