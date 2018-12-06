from flask import request, jsonify
import datetime
import time
import jwt

from api.models.user_model import User
from user_view import users_db
from functools import wraps

secret_key = "klgwso7dbnc37hgv8oiawb/we9h7_hywg8"
#
# users_db = [
#     User(
#         name={"firstName":"Emmanuel", "lastName":"Matembu",\
#          "otherName":"Dominic"},
#         userName="Manuel",
#         email="ematembu@gmal.com",
#         phoneNumber=256700701616,
#         password="manuel123"
#         # date="2018-11-25 22:41:14"
#         )]
# users_db[0].isAdmin = True


def encode_token(userId):
    token = jwt.encode({'userId': User.userId,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=5)},
        secret_key)
    return token

def decode_token(token):
    define = jwt.decode(token, secret_key, algorithms=['HS256'])
    return define

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['token']
            try:
                decoded = decode_token(token)
                return fuct(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "token expired"}), 401
            except jwt.InvalidSignatureError:
                return jsonify({"message": "Signature verification failed"}), 401
            except jwt.InvalidTokeneError:
                return jsonify({"message": "Invalid Token verification failed"}), 401
        except KeyError:
            return jsonify({"message": "Missing token"}), 401
        return wrapper

def get_current_user():
    """Fetches current user details from database"""
    token = request.headers['token']
    decode_token = decode_token(token)
    try:
        user_id = decode_token[User.userId]
        return users_db[User.userName]
    except KeyError:
        return jsonify({"message":"user_id not in token"}), 401

def admin_required(func):
    """This decorator limits access to the routes to admin user only"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        isAdmin = get_current_user()['isAdmin']
        if isAdmin:
            return func(*args, **kwargs)
        return jsonify({"messsage":"Only admin can access this route"}), 401
    return wrapper

def non_admin_required(func):
    """This decorator limits access to the routes to non admin user only"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        isAdmin = get_current_user()['isAdmin']
        if not isAdmin:
            return jsonify({"messsage":"Only Non admin can access this route"}), 401
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    Manuel=User()
    Manuel.get_current_user(name={"firstName":"Emmanuel", "lastName":"Matembu",\
     "otherName":"Dominic"}, userName="Manuel", email="ematembu@gmal.com", \
     phoneNumber=256700701616,password="manuel123")
