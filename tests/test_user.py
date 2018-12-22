import json
import unittest
from api.views.user_view import user_bp
from api.helpers.auth import encode_token
from api.app import app

new_user = {
    "email": "ematembu@gmail.com",
    "firstName": "manuel",
    "lastName": "Dominic",
    "otherName": "highway",
    "password": "manuel123",
    "phoneNumber": "256700701616",
    "userName": "mats"
}
new_msg = {
    "email": "ematembu@gmail.com",
    "firstName": "manuel",
    "lastName": "Dominic",
    "otherName": "highway",
    "userId": 2,
    "phoneNumber": "256700701616",
    "userName": "mats",
    "isAdmin":false
}

users_list = {
    "email": "ematembu@gmail.com",
    "firstName": "manuel",
    "lastName": "Dominic",
    "otherName": "highway",
    "password": "manuel123",
    "phoneNumber": "256700701616",
    "userName": "mats"
}

new_user_response = {
    "status": 201,
    "message": "Successfully registered",
    "users": new_msg}

login_user = {
    "email": "admin@ireporter.com",
    "password": "admin123"
}

login_user_response = {
    "Token": encode_token(userId),
    "message": "Successfully logged In"}


class TestUser(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_sign_up(self):
        response = self.app.post('/api/v1/auth/signup', content_type="application/json", data=json.dumps(new_user))
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_user_response)

    def test_login(self):
        response = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(login_user))
        data = response.data.decode()
        self.assertEqual(json.loads(data), login_user_response)

    def test_get_users(self):
        response = self.app.get('/api/v1/auth/login')
        data = response.data.decode()
        message = {"status": 200, "users": users_list}
        self.assertEqual(json.loads(data), message)


if __name__ == '__main__':
    unittest.main()
