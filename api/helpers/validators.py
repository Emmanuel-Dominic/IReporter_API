from functools import wraps
import string
import re
from flask import request,jsonify

example_login_data = {"email":"Your email","password":"Your password"}
example_signup_data = {
    "firstName":"Your firstName",
    "lastName":"Your lastName",
    "otherName":"Your otherName",
    "email":"Your email",
    "phoneNumber":"Your phoneNumber",
    "password":"Your password",
    "userName":"Your userName"
    }
invalid_key_msg = "Invalid Key in data,please provide valid input data"
required_feild = "field is Required"
Invalid_value_input = "Invalid input value"
def verify_login_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": "Please provide data",
                "example":example_login_data}),400
        # try:
        #     data = request.get_json()
        #     if not data["email"]:
        #         return jsonify({"message":"email {}".format(required_feild)}), 406
        #     elif data["email"].isspace():
        #         return jsonify({"message":"{} at email".format(Invalid_value_input)}), 406
        #     elif data["password"].isspace():
        #         return jsonify({"message":"{} at password".format(Invalid_value_input)}), 406
        #     elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
        #         return jsonify({"message":"Your email address is not valid."}), 406
        #
        # except AttributeError:
        #     return jsonify({"message":"Please provide valid field for string data",
        #         "example":example_signup_data}),400
        # except AttributeError:
        #     return jsonify({"message":"Please provide valid field for string data",
        #         "example":example_signup_data}),400
        
        # if data is not of type application/json
        try:
            data = request.get_json()
        except:
            return jsonify({"message":"Please provide JSON data",
                "example":example_login_data}),400

        # if does not contain valid keys
        try:
            data = request.get_json()
            password=data["password"]
            email=data["email"]
        except KeyError:
            return jsonify({"message":invalid_key_msg,
                "example":example_login_data}), 400
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
            if not data["firstName"]:
                return jsonify({"message":"firstName {}".format(required_feild)}), 406
            elif not data["password"]:
                return jsonify({"message":"password {}".format(required_feild)}), 406
            elif not data["lastName"]:
                return jsonify({"message":"lastName {}".format(required_feild)}), 406
            elif not data["email"]:
                return jsonify({"message":"email {}".format(required_feild)}), 406
            elif not data["phoneNumber"]:
                return jsonify({"message":"phoneNumber {}".format(required_feild)}), 406
            elif not data["userName"]:
                return jsonify({"message":"userName {}".format(required_feild)}), 406
            elif len(data["password"]) < 6:
                return jsonify({"message":"Password must be atleast six characters or more"}), 406
            elif data["firstName"].isspace():
                return jsonify({"message":"{} at firstName".format(Invalid_value_input)}), 406
            elif data["lastName"].isspace():
                return jsonify({"message":"{} at lastName".format(Invalid_value_input)}), 406
            elif data["email"].isspace():
                return jsonify({"message":"{} at email".format(Invalid_value_input)}), 406
            elif data["phoneNumber"].isspace():
                return jsonify({"message":"{} at phoneNumber".format(Invalid_value_input)}), 406
            elif data["password"].isspace():
                return jsonify({"message":"{} at password".format(Invalid_value_input)}), 406
            elif data["userName"].isspace():
                return jsonify({"message":"{} at userName".format(Invalid_value_input)}), 406
            elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
                return jsonify({"message":"Your email address is not valid."}), 406

        except AttributeError:
            return jsonify({"message":"Please provide valid field for string data",
                "example":example_signup_data}),400
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
