import datetime
from functools import wraps
import jwt
from flask import request, jsonify
from api.models.database_model import DatabaseConnection
import psycopg2


secret_key = "softwareDeveloper.Manuel@secret_key/mats.com"

db=DatabaseConnection()


def encode_token(user_id):
    token = jwt.encode({'userId': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
        secret_key).decode('utf-8')
    return token

def decode_token(token):
    decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    return decoded_token

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            token_in_header = request.headers['token']
            try:
                decoded = decode_token(token_in_header)
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
    user_id = decoded_token["userId"]
    sql_command="""SELECT user_id,isadmin  FROM users WHERE user_id='{}'""".format(user_id)
    db.cursor.execute(sql_command)
    the_id=db.cursor.fetchone()
    return {"userId": the_id["user_id"], "isadmin": the_id["isadmin"]}



def admin_required(func):
    """This decorator limits access to the routes to admin user only"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            isAdmin = get_current_user()["isadmin"]
        except TypeError:
            return jsonify({"Message":"Invalid token or user not found"})
        if isAdmin == False:
            return jsonify({"messsage": "Only admin can access this route"}), 401
        return func(*args, **kwargs)
    return wrapper

def non_admin_required(func):
    """This decorator limits access to the routes to non admin user only"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            isAdmin = get_current_user()["isadmin"]
        except TypeError:
            return jsonify({"Message":"Invalid token or user not found"})
        if isAdmin == True:
            return jsonify({"messsage": "Only Non admin can access this route"}), 401
        return func(*args, **kwargs)
    return wrapper


def encode_token_test(userId):
    token = jwt.encode({'userId': userId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=20)},
        "secret_key")
    return token