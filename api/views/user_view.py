
"""views file for users, login, signup and logout sessions"""

from flask import Blueprint, jsonify, request, Response, json
from models.user_model import User,users_table
from .auth_helper import encode_token
from helpers.validators import verify_login_data


from functools import wraps



user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1')


@user_bp.route('/users', methods=['GET'])
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
def sign_up():
    data = request.get_json()
    try:
        name = {"firstName": data['firstName'], "lastName": data['lastName'], \
                "otherName": data['otherName']}
        email = data['email']
        phoneNumber = data['phoneNumber']
        password = data['password']
        userName = data['userName']
    except KeyError:
        return jsonify({"message": "Key input error"}), 400
    for user in users_table:
        if email == user.email:
            return jsonify({"message": "Email exists"}), 406
    new_user = User(userName=userName, \
                    name=name, email=email, \
                    phoneNumber=phoneNumber, \
                    password=password \
                    )
    users_table.append(new_user)
    return jsonify({"status": 201, "users": data}), 201


@user_bp.route('/auth/login', methods=['POST'])
@verify_login_data
def login():
    data = request.get_json()

    # try:
    password = data['password']
    email = data['email']
    # except KeyError:
        # return jsonify({"message": "Key input error"}), 400

    for user_obj in users_table:
        if email == user_obj.email and password == user_obj.password:
            return jsonify({"Token": encode_token(user_obj.userId), "message": "Successfully logged In"})

    return jsonify({"message": "Invalid credentials, Please try again"}), 401
