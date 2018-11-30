"""views file for users, login, signup and logout sessions"""
from flask import Blueprint, jsonify, request, Response, json
from api.models.user_model import User


user_bp = Blueprint('user_bp', __name__, url_prefix='/api/v1')

users_db = [
    User(
        name={"firstName":"Emmanuel", "lastName":"Matembu",\
         "otherName":"Dominic"},
        userName="Manuel",
        email="ematembu@gmal.com",
        phoneNumber=256700701616,
        password="manuel123"
        # date="2018-11-25 22:41:14"
        ),
    User(
        name={"firstName":"Joseph", "lastName":"Wamono",\
         "otherName":"Mungoma"},
        userName="Jose",
        email="ematembu@gmal.com",
        phoneNumber=256788084708,
        password="Jose12345"
        # date="2018-11-26 21:41:17"
        ),
    User(
        name={"firstName":"Annmary", "lastName":"Mukite",\
         "otherName":"Muhwana"},
        userName="MaryAnn",
        email="ematembu@gmal.com",
        phoneNumber=256773329287,
        password="Annmary15"
        # date="2018-11-29 20:41:13"
        ),
]

users_db[0].isAdmin = True

@user_bp.route('/users', methods=['GET'])
def get_users():
    """docstring function that return all users detials"""
    users_list = []
    for user in users_db[1:]:
        users_list.append(user.get_user_details())
    return jsonify({
        "status": 200,
        "users": users_list
    }), 200

@user_bp.route('/signup', methods=['POST'])
def sign_up():
    for person in users_db:
        if person['email'] != user.email:
            data = request.get_json()
            name = {"firstName":data['firstName'], "lastName":data['lastName'],\
             "otherName":data['lastName']}
            users_db.append(
                User(name=name, email=data['email'],\
                    phoneNumber=data['phoneNumber'], password=data['password'],\
                    userName=data['userName'], date=data['date'],\
                    userId=data['userId']))
            return jsonify({
                "status": 200,
                "users": users_db[:-1].get_user_details()
            }), 200

        return jsonify({
            "status": 404,
            "error": "bad request"
        }), 200
