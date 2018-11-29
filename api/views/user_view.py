from flask import Flask, jsonify, request
# , make_response
import uuid
# from  flask_sqlalchemy import SQLAIchemy
from werkzeug.security import generate_password_hash, check_password_hash
# from functools import wraps
import jwt
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'
app.config['SQLASCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/api/todo.db'


db = SQLAlchemy(app)
# db = []

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

    # public_id = public_id
    # name = name
    # id = id
    # # User.id += 1
    # admin = False
    # password = password


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(50))
    user_id = db.Column(db.Integer)
    complete = db.Column(db.Boolean)

#
# users_db = [
#     User(
#         name={"firstName":"Emmanuel", "lastName":"Matembu",\
#          "otherName":"Dominic"},
#         userName="Manuel",
#         email="ematembu@gmal.com",
#         phoneNumber=256700701616,
#         password="manuel123",
#         # date="2018-11-25 22:41:14"
#         ),
#     User(
#         name={"firstName":"Joseph", "lastName":"Wamono",\
#          "otherName":"Mungoma"},
#         userName="Jose",
#         email="ematembu@gmal.com",
#         phoneNumber=256788084708,
#         password="Jose12345",
#         # date="2018-11-26 21:41:17"
#         ),
#     User(
#         name={"firstName":"Annmary", "lastName":"Mukite",\
#          "otherName":"Muhwana"},
#         userName="MaryAnn",
#         email="ematembu@gmal.com",
#         phoneNumber=256773329287,
#         password="Annmary15",
#         # date="2018-11-29 20:41:13"
#         ),
# ]
#
# users_db[0].isAdmin = True

@app.route('/users', methods=['GET'])
def get_all_users():
    """docstring function that return all users detials"""
    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'users': output})
    # users_list = []
    # for user in users_db[1:]:
    #     users_list.append(user.get_user_details())
    # return jsonify({
    #     "status": 200,
    #     "users": users_list
    # }), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_users():
    """docstring function that return all users detials"""
    return ''
    # users_list = []
    # for user in users_db[1:]:
    #     users_list.append(user.get_user_details())
    # return jsonify({
    #     "status": 200,
    #     "users": users_list
    # }), 200

@app.route('/users', methods=['GET'])
def sign_up():
    """docstring function that return all users detials"""
    data = request.get_json()

    hash_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(publuic_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user Created!'})
    # users_list = []
    # for user in users_db[1:]:
    #     users_list.append(user.get_user_details())
    # return jsonify({
    #     "status": 200,
    #     "users": users_list
    # }), 200


@app.route('/users/<int:user_id>', methods=['POST'])
def promote_user():
    return ''


@app.route('/users/<int:user_id>', methods=['POST'])
def delete_user():
    return ''
    # for person in users_db:
    #     if person['email'] != user.email:
    #         data = request.get_json()
    #         name = {"firstName":data['firstName'], "lastName":data['lastName'],\
    #          "otherName":data['lastName']}
    #         users_db.append(
    #             User(name=name, email=data['email'],\
    #                 phoneNumber=data['phoneNumber'], password=data['password'],\
    #                 userName=data['userName'], date=data['date'],\
    #                 userId=data['userId']))
    #         return jsonify({
    #             "status": 200,
    #             "users": users_db[:-1].get_user_details()
    #         }), 200
    #
    #     return jsonify({
    #         "status": 404,
    #         "error": "bad request"
    #     }), 200









#
#
#
#
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
#
#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 403
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 403
#         return f(*args, **kwargs)
#     return decorated
#
#
# @app.route('/unprotected')
# def unprotected():
#     return jsonify({'message': 'Anyone can view this'})
#
# @app.route('/protected')
# @token_required
# def protected():
#     return jsonify({'message': 'This is only available for people with validtokens.'})
#
# @app.route('/login')
# def login():
#     auth = request.authorization
#
#     if auth and auth.password == 'password':
#         token = jwt.dump({'user':auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds = 10)}, app.config['SECRET_KEY'])
#         # return jsonify({'token': token.decode('UTF-8')})
#     return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="LOGIN rEQUIRED"'})
#
# #
# # @app.route('/unprotected')
# # def unprotected():
# #     return ''
# #
# # @app.route('/unprotected')
# # def unprotected():
# #     return ''
# #
# # @app.route('/unprotected')
# # def unprotected():
# #     return ''
# #
# #
# # @app.route('/unprotected')
# # def unprotected():
# #     return ''
# # # app.config['SECRETE_KEY'] = 'thisissecret'
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/api/todo.db'
# # #
# # # db = SQLAIchemy(app)
# # #
# # # class User(db.Model):
# # #     id

if __name__ == '__main__':
    app.run(debug=True)
