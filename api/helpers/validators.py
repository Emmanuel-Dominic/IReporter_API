from functools import wraps
import string
from flask import request,jsonify

example_login_data = {"email":"Your email","password":"Your password"}
example_signup_data = {"email":"Your email","password":"Your password"}
invalid_key_msg = "Invalid Key in data,please provide valid input data"

def verify_login_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "Please provide data",
                "example":example_login_data}),400

        # if data is not of type application/json
        try:
            data = request.get_json()
        except:
            return jsonify({"message":"Please provide JSON data",
                "example":example_login_data}),400

        # if does not contain valid keys
        try:
            data['password']
            data['email']
        except KeyError:
            return jsonify({"message":invalid_key_msg,
                "example":example_login_data}), 400
        return func(*args , **kwargs)
    return wrapper
