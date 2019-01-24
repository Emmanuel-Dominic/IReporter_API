from flask import Blueprint, jsonify, request
from api.helpers.auth import encode_token, admin_required, token_required
from api.helpers.validators import verify_login_data, verify_signup_data
from api.models.database_model import DatabaseConnection
from api.helpers.auth import admin_required, non_admin_required
from api.controllers.user_controller import get_all_users, signup_user, user_login_check
from werkzeug.security import check_password_hash

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/v1")

db = DatabaseConnection()


@user_bp.route("/users", methods=["GET"])
@token_required
@admin_required
def get_users():
    """docstring function that return all users detials"""
    users = get_all_users()
    # if len(users)>0:
    if users:
        return jsonify({"status": 200, "data": [users]}), 200
    return bad_request()


@user_bp.route("/auth/signup", methods=["POST"])
@verify_signup_data
def user_signup():
    detail = signup_user()
    if detail:
        return jsonify({"status": 201, "token": encode_token(detail["user_id"]),
                        "data": detail, "message": "Successfully registered"}), 201
    return bad_request()


@user_bp.route("/auth/login", methods=["POST"])
@verify_login_data
def user_login():
    data = request.get_json()
    user = user_login_check()
    if user and check_password_hash(user["passwd"], data["password"]):
        return jsonify({"token": encode_token(user["user_id"]),
                        "message": "Successfully logged In"}), 200
    return jsonify({"message": "Invalid credentials, Please try again"}), 401


def bad_request():
    return jsonify({"status": 400, "error": "Sorry, Bad request"}), 400
