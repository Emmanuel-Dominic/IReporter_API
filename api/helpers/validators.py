from functools import wraps
import re
from flask import request,jsonify


example_login_data = {"email":"Your email","password":"Your password"}
example_signup_data = {
    "firstName":"Your firstName", "lastName":"Your lastName", \
    "otherName":"Your otherName", "email":"Your email", \
    "phoneNumber":"Your phoneNumber", "password":"Your password", \
    "userName":"Your userName"
    }
example_create_data = {"comment": "comment","images": "image name",
        "locationLat": 0.111111,"locationLong": 0.1111111,"videos": "video name"}
invalid_key_msg = "Invalid Key in data,please provide valid input data"
required_feild = "field is Required"
Invalid_value_msg = "Invalid value in data,please provide valid input data"
get_data="Please provide data"
data_string="Please provide valid field for string data"
valid_type="Please provide valid data type for fields"
json_data="Please provide JSON data"


def verify_password_and_email():
    """verify password and email in user records"""
    data = request.get_json()
    if len(data["password"]) < 6:
        response = jsonify({"message":"Password must be atleast six characters or more"}), 406
    elif not data["password"]:
        response = jsonify({"message":"password {}".format(required_feild)}), 406
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
        response = jsonify({"message":"Your email address is not valid."}), 406


def verify_login_data(func):
    """Decorator for verifying user records at login"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.get_json():
            return jsonify({"message": get_data,
                "example":example_login_data}),400
        # if data is not of type application/json
        error = None
        try:
            data = request.get_json()
            verify = verify_password_and_email()
            response = None
            if verify:
                response = verify   
            else:
                response = func(*args , **kwargs)
            return response
        # if does not contain valid keys
        except KeyError:
            error = jsonify({"message":invalid_key_msg,
                "example":example_login_data}), 400
        except ValueError:
            error = jsonify({"message":valid_type,
                "example":example_login_data}),406
        return error
    return wrapper


def verify_signup_data(func):
    """Decorator for verifying user records at signup"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.get_json():
            return jsonify({"message": get_data,
                "example":example_signup_data}),400
        # if data is not of type application/json
        error = None
        try:
            data = request.get_json()
            verify = verify_password_and_email()
            response = None
            if not data["firstName"].isalpha():
                response = jsonify({"message":"{} string at firstName".format(Invalid_value_msg)}), 406
            elif not data["firstName"]:
                response = jsonify({"message":"firstName feild is required"}), 406
            elif not data["lastName"].isalpha():
                response = jsonify({"message":"{} string at lastName".format(Invalid_value_msg)}), 406
            elif not data["lastName"]:
                response = jsonify({"message":"lastName feild is required"}), 406
            elif not isinstance(data["otherName"],str):
                response = jsonify({"message":"Invalid, otherName must be a string"}),406
            elif not data["userName"].isalpha():
                response = jsonify({"message":"{} at userName".format(Invalid_value_msg)}), 406
            elif not data["userName"]:
                response = jsonify({"message":"userName {}".format(required_feild)}), 406
            elif not isinstance(data["phoneNumber"],int):
                response = jsonify({"error":"Invalid, must be a phone number"}), 406
            elif not data["phoneNumber"]:
                response = jsonify({"message":"phoneNumber feild is required"}), 406
            elif verify:
                response = verify
            else:
                response = func(*args , **kwargs)
            return response
        # if does not contain valid keys
        except KeyError:
            error = jsonify({"message":invalid_key_msg,
                "example":example_signup_data}), 400
        except ValueError:
            error = jsonify({"message":valid_type,
                "example":example_signup_data}),400
        return error
    return wrapper



def verify_create_incident_data(func):
    """Decorator for verifying user records at create incident"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": get_data,
                "example":example_create_data}),400
        # if data is not of type application/json
        error = None
        try:
            data = request.get_json()
            response = None
            images=data['images']
            videos=data['videos']
            if not isinstance(data["locationLong"],float):
                response = jsonify({"message":"Invalid, locationLong must be a float"}),406
            elif not data["locationLong"]:
                response = jsonify({"message":"locationLong feild is required"}), 406
            elif not isinstance(data["locationLat"],float):
                response = jsonify({"message":"Invalid, locationLat must be a float"}),406
            elif not data["locationLat"]:
                response = jsonify({"message":"locationLat feild is required"}), 406
            elif not isinstance(data["comment"],str):
                response = jsonify({"message":"Invalid, comment must be a string"}),406
            elif not data["comment"]:
                response = jsonify({"message":"comment feild is required"}), 406
            else:
                response = func(*args, **kwargs)
            return response
        # if does not contain valid keys
        except KeyError:
            error = jsonify({"message":invalid_key_msg,
                "example":example_create_data}), 400
        except ValueError:
            error = jsonify({"message":valid_type,
                "example":example_create_data}),400
        return error
    return wrapper
