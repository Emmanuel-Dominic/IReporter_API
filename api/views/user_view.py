"""views file for users, login, signup and logout sessions"""
from flask import Blueprint, jsonify, request, Response, json
from api.models.user_model import User
# from api.views.auth_helper import token_required,non_admin_required,admin_required


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
        email="ematembu1@gmal.com",
        phoneNumber=256788084708,
        password="Jose12345"
        # date="2018-11-26 21:41:17"
        ),
    User(
        name={"firstName":"Annmary", "lastName":"Mukite",\
         "otherName":"Muhwana"},\
        userName="MaryAnn",\
        email="ematembu2@gmal.com",\
        phoneNumber=256773329287,\
        password="Annmary15" )
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
    data = request.get_json()
    try:
        name = {"firstName":data['firstName'], "lastName":data['lastName'],\
         "otherName":data['otherName']}
        email=data['email']
        phoneNumber=data['phoneNumber']
        password=data['password']
        userName=data['userName']
    except KeyError:
        return jsonify({"message": "Key input error"}),400


    for user in users_db:
        if email == user.email:
            return jsonify({"message":"Email exists"}),406
    new_user = User(userName=userName,\
        name=name,email=email,\
        phoneNumber=phoneNumber,\
        password =password\
    )
    users_db.append(new_user)
    return jsonify({"status": 201,"users": data }), 201
