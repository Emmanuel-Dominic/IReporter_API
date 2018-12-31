import datetime
from functools import wraps
import jwt
from flask import request, jsonify
from api.models.user_model import User, users_table

secret_key = "softwareDeveloper.Manuel@secret_key/mats.com"


def encode_token(userId):
    token = jwt.encode({'userId': userId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)},
        secret_key).decode('utf-8')
    return token

def decode_token(token):
    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    return decoded_token

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['token']
            try:
                decoded = decode_token(token)
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "token expired"}), 401
            except jwt.InvalidSignatureError:
                return jsonify({"message": "Signature verification failed"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token verification failed"}), 401
        except KeyError:
            return jsonify({"message": "Missing token"}), 401
        return func(*args, **kwargs)


    return wrapper


def get_current_user():
    """Fetches current user details from table"""
    token = request.headers['token']
    decoded_token = decode_token(token)
    # try:
    userId = decoded_token["userId"]
    for user_obj in users_table:
        if user_obj.userId == userId:
            return {"userId": userId, "isAdmin": user_obj.isAdmin}
    # except KeyError:
    #     return jsonify({"message": "userId not in token"}), 401



def admin_required(func):
    """This decorator limits access to the routes to admin user only"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        isAdmin = get_current_user()["isAdmin"]
        if isAdmin == False:
            return jsonify({"messsage": "Only admin can access this route"}), 401
        return func(*args, **kwargs)
    return wrapper

def non_admin_required(func):
    """This decorator limits access to the routes to non admin user only"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        isAdmin = get_current_user()["isAdmin"]
        if isAdmin == True:
            return jsonify({"messsage": "Only Non admin can access this route"}), 401
        return func(*args, **kwargs)
    return wrapper
