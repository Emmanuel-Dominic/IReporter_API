import re
from functools import wraps

from flask import request, jsonify

example_login_data = {"email": "Your_email", "password": "Your_password"}
example_signup_data = {
    "firstName": "Your_firstName", "lastName": "Your_lastName", \
    "otherName": "Your_otherName", "email": "Your_email", \
    "phoneNumber": "Your_phoneNumber", "password": "Your_password", \
    "userName": "Your_userName"
}
example_create_data = {
    "title": "title",
    "comment": "comment",
    "images": "1.jpeg",
    "longtitude": 6.66666,
    "latitude": 7.7777,
    "videos": "1.gif"
}
invalid_key_msg = "Invalid Key in data,please provide valid input data"
required_feild = "field is Required"
Invalid_value_msg = "Invalid value in data,please provide valid input data"
get_data = "Please provide data"
data_string = "Please provide valid field for string data"
valid_type = "Please provide valid data type for fields"
json_data = "Please provide JSON data"


def bad_request():
    return jsonify({"status": 400, "error": "Sorry, Bad request"}), 400


def not_found():
    return jsonify({"status": 404, "error": "Sorry, Incident Not Found"}), 404


def not_data():
    return jsonify({"status": 406, "error": "Sorry, no input data found"}), 406


def pass_email():
    data = request.get_json()
    response = None
    if len(data["password"]) < 6:
        response = jsonify({"message": "Password must be atleast six characters or more"}), 406
    elif not data["password"]:
        response = jsonify({"message": "password {}".format(required_feild)}), 406
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data["email"]):
        response = jsonify({"message": "Your email address is not valid."}), 406
    return response


def verify_login_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.get_json():
            return jsonify({"message": get_data,
                            "example": example_login_data}), 400
        # if data is not of type application/json
        error = None
        try:
            data = request.get_json()
            verify = pass_email()
            response = None
            if verify:
                return verify
            else:
                response = func(*args, **kwargs)
            return response
        # if does not contain valid keys
        except KeyError:
            error = jsonify({"message": invalid_key_msg,
                             "example": example_login_data}), 400
        except ValueError:
            error = jsonify({"message": valid_type,
                             "example": example_login_data}), 406
        return error

    return wrapper


def verify_signup_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.get_json():
            return jsonify({"message": get_data,
                            "example": example_signup_data}), 400
        # if data is not of type application/json
        error = None
        try:
            data = request.get_json()
            verify = pass_email()
            response = None
            if verify:
                response = verify
            elif not data["firstName"].isalpha():
                response = jsonify({"message": "{} string at firstName".format(Invalid_value_msg)}), 406
            elif not data["firstName"]:
                response = jsonify({"message": "firstName feild is required"}), 406
            elif not data["lastName"].isalpha():
                response = jsonify({"message": "{} string at lastName".format(Invalid_value_msg)}), 406
            elif not data["lastName"]:
                response = jsonify({"message": "lastName feild is required"}), 406
            elif not isinstance(data["otherName"], str):
                response = jsonify({"message": "Invalid, otherName must be a string"}), 406
            elif not data["userName"].isalpha():
                response = jsonify({"message": "{} at userName".format(Invalid_value_msg)}), 406
            elif not data["userName"]:
                response = jsonify({"message": "userName {}".format(required_feild)}), 406
            elif not isinstance(data["phoneNumber"], int):
                response = jsonify({"error": "Invalid, must be a phone number"}), 406
            elif not data["phoneNumber"]:
                response = jsonify({"message": "phoneNumber feild is required"}), 406
            else:
                response = func(*args, **kwargs)
            return response
        # if does not contain valid keys
        except KeyError:
            error = jsonify({"message": invalid_key_msg,
                             "example": example_signup_data}), 400
        except ValueError:
            error = jsonify({"message": valid_type,
                             "example": example_signup_data}), 400
        except TypeError:
            error = jsonify({"message": "Email already in use"}), 406
        return error

    return wrapper


def verify_create_incident_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data:
            return jsonify({"message": get_data,
                            "example": example_create_data}), 400
        # if data is not of type application/json
        error = None
        try:
            data = request.get_json()
            response = None
            if not isinstance(data["longtitude"], float):
                response = jsonify({"message": "Invalid, longtitude must be a float"}), 406
            elif not data["longtitude"]:
                response = jsonify({"message": "longtitude feild is required"}), 406
            elif not isinstance(data["latitude"], float):
                response = jsonify({"message": "Invalid, latitude must be a float"}), 406
            elif not data["latitude"]:
                response = jsonify({"message": "latitude feild is required"}), 406
            elif not isinstance(data['videos'], str):
                response = jsonify({"message": "Invalid, video name must be a string"}), 406
            elif not isinstance(data['images'], str):
                response = jsonify({"message": "Invalid, image name must be a string"}), 406
            elif not isinstance(data["comment"], str):
                response = jsonify({"message": "Invalid, comment must be a string"}), 406
            elif not data["comment"]:
                response = jsonify({"message": "comment feild is required"}), 406
            elif not data["title"].isalpha():
                response = jsonify({"message": "title feild should have only alphabets"}), 406
            else:
                response = func(*args, **kwargs)
            return response
        # if does not contain valid keys
        except KeyError:
            error = jsonify({"message": invalid_key_msg,
                             "example": example_create_data}), 400
        except ValueError:
            error = jsonify({"message": valid_type,
                             "example": example_create_data}), 400
        except TypeError:
            error = jsonify({"message": "Incident already exist"}), 406
        return error

    return wrapper
