from functools import wraps
import string
import re
from flask import request,jsonify


example_login_data = {"email":"Your email","password":"Your password"}
example_signup_data = {
    "firstName":"Your firstName", "lastName":"Your lastName", \
    "otherName":"Your otherName", "email":"Your email", \
    "phoneNumber":"Your phoneNumber", "password":"Your password", \
    "userName":"Your userName"
    }
invalid_key_msg = "Invalid Key in data,please provide valid input data"
required_feild = "field is Required"
Invalid_value_msg = "Invalid value in data,please provide valid input data"

def get_password(password):
    data = request.get_json()
    if len(data["password"]) < 6:
        return jsonify({"message":"Password must be atleast six characters or more"}), 406
    if data["password"].isspace():
        return jsonify({"message":"{} at password".format(Invalid_value_msg)}), 406
    if not data["password"]:
        return jsonify({"message":"password {}".format(required_feild)}), 406

def get_email(email):
    data = request.get_json()
    if data["email"].isspace():
        return jsonify({"message":"{} at email".format(Invalid_value_msg)}), 406
    if not data["email"]:
        return jsonify({"message":"email {}".format(required_feild)}), 406

def get_userName(userName):
    data = request.get_json()
    if not data["userName"]:
        return jsonify({"message":"userName {}".format(required_feild)}), 406
    if not data["userName"].isalpha():
        return jsonify({"message":"{} at userName".format(Invalid_value_msg)}), 406

def get_phoneNumber(phoneNumber):
    data = request.get_json()
    if not data["phoneNumber"]:
        return jsonify({"message":"phoneNumber feild is required"}), 406



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
        # try:
        #     data = request.get_json()
        #     password=data["password"]
        #     email=data["email"]
        # except KeyError:
        #     return jsonify({"message":invalid_key_msg,
        #         "example":example_login_data}), 400
        return func(*args , **kwargs)
    return wrapper


def verify_signup_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "Please provide data",
                "example":example_signup_data}),400
        # if data is not of type application/json
        try:
            data = request.get_json()
            name = {"firstName":data["firstName"],"lastName":data["lastName"],"otherName":"otherName"}
            email = data["email"]
            password = data["password"]
            phoneNumber = data["phoneNumber"]
            userName = data["userName"]
            if not data["firstName"]:
                return jsonify({"message":"firstName {}".format(required_feild)}), 406
            if not data["lastName"]:
                return jsonify({"message":"lastName {}".format(required_feild)}), 406
            if not data["firstName"].isalpha():
                return jsonify({"message":"{} at firstName".format(Invalid_value_msg)}), 406
            if not data["lastName"].isalpha():
                return jsonify({"message":"{} at lastName".format(Invalid_value_msg)}), 406

            # get_user_names(firstName,lastName,otherName)
            get_password(password)
            get_email(email)
            get_userName(userName)
            get_phoneNumber(phoneNumber)
        except AttributeError:
            return jsonify({"message":"Please provide valid field for string data",
                "example":example_signup_data}),400
        except ValueError:
            return jsonify({"message":"Please provide valid data type for fields",
                "example":example_signup_data}),406
        except:
            return jsonify({"message":"Please provide JSON data",
                "example":example_signup_data}),400

        # if does not contain valid keys
        try:
            name = {"firstName": data["firstName"], "lastName": data["lastName"], \
                    "otherName": data["otherName"]}
            email = data["email"]
            phoneNumber = data["phoneNumber"]
            password = data["phoneNumber"]
            userName = data["userName"]
        except KeyError:
            return jsonify({"message":invalid_key_msg,
                "example":example_signup_data}), 400

        return func(*args , **kwargs)
    return wrapper
