import os
import unittest
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.helpers.auth import encode_token
# from api.models.incident_model import intervention_list,redflag_list
from api.app import app
import jwt
import datetime


class TestBase(unittest.TestCase):
    """docstring for TestBase class"""
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()        


new_user = {
"email": "ematembu@ireporter.com",
"firstName": "manuel",
"lastName": "Dominic",
"otherName": "highway",
"password": "manuel123",
"phoneNumber": 256700701616,
"userName": "mats"
}

new_user_error_mail={
"email": "ematembu@ireporter.com",
"firstName": "manuel",
"lastName": "Dominic",
"otherName": "highway",
"password": "manuel123",
"phoneNumber": 256700701616,
"userName": "mats"
}

new_user_response = {"status": 201,
    "message": "Successfully registered",
    "user": {
        "email": "ematembu@ireporter.com",
        "isAdmin": False,
        "name": "manuel Dominic highway",
        "phoneNumber": 256700701616,
        "userId": 2,
        "userName": "mats"
    }
}

login_user = {
    "password": "admin123",
    "email": "admin@ireporter.com"
}

invalid_login_user={
    "password": "admin589",
    "email": "admin@ireporter.com"
}

new_status={
  "status":"Rejected"
}

login_user_response = {
    "token": encode_token(2),
    "message": "Successfully logged In"}

all_users_response = {
    "status": 200,
    "users": [
{
"email": "ematembu@ireporter.com",
"firstName": "manuel",
"lastName": "Dominic",
"otherName": "highway",
"password": "manuel123",
"phoneNumber": 256700701616,
"userName": "mats"
}]
}

new_intervention = {
    "comment": "Jinja bridge needs construction",
    "createdBy": 2,
    "images": "1.jpeg",
    "locationLong": 6.66666,
    "locationLat": 7.7777,
    "type": "intervention",
    "videos": "1.gif"
}

new_intervention_response = {
    "data": [
        {
            "id": 1,
            "message": "Created intervention record"
        }
    ],
    "status": 201
}

new_intervention1 = {
    "comment": "Mbarara highway needs construction",
    "createdOn": "Fri, 30 Nov 2018 12:09:32 GMT",
    "images": "1.jpeg",
    "locationLat": 5.38974,
    "locationLong": 0.33737,
    "type": "intervention",
    "videos": "1.gif"
}

new_intervention1_response = {
    "data": [
        {
            "id": 2,
            "message": "Created intervention record"
        }
    ],
    "status": 201
}

example_create_data={"comment": "comment","images": "image name",
        "locationLat": 0.111111,"locationLong": 0.1111111,"videos": "video name"}
invalid_key_msg = "Invalid Key in data,please provide valid input data"

new_location = {
    "locationLong": 8.555555,
    "locationLat": 5.88289
}
new_comment = {"comment": "Sorry!, error information"}

new_redflag = {
"comment": "james was caught idle and disorderly",
"images": "1.jpeg",
"locationLat": 5.38974,
"locationLong": 0.33737,
"type": "red-flag",
"videos": "1.gif"

}


new_redflag_response = {
    "data": [
        {
            "id": 2,
            "message": "Created redflag record"
        }
    ],
    "status": 201
}


new_redflag1 = {
"comment": "Arnold was caught taking jack fruit in hassan's Garden",
"createdBy": 2,
"images": "1.jpeg",
"locationLong": 6.66666,
"locationLat": 7.7777,
"type": "redflag",
"videos": "1.gif"

}

new_redflag1_response = {
    "data": [
        {
            "id": 1,
            "message": "Created redflag record"
        }
    ],
    "status": 201
}

new_error_redflag={
"comment": "Arnold was caught stealing jack fruit in hassan's Garden",
"locationLong": 6.66666,
"locationLat": 7.7777,
"type": "redflag",
"videos": "1.gif"

}

new_error_intervention={
    "comment": "Jinja bridge needs construction",
    "locationLong": 6.66666,
    "locationLat": 7.7777,
    "type": "redflag",
    "videos": "1.gif"

}


new_bad_redflag={}

new_bad_intervention={}


error = {"status":404, "error": "Sorry, Incident Not Found"}


def get_incidents_by_type(incident_type):
    all_incidents = []
    for incident in incident_table:
        if incident.type == incident_type:
            all_incidents.append(
                {
                    "comment": incident.comment,
                    "createdBy": incident.createdBy,
                    "createdOn": incident.createdOn,
                    "images": incident.images,
                    "incidentId": incident.incidentId,
                    "location": " ".join([incident.locationLong, ',', incident.locationLat]),
                    "status": incident.status,
                    "type": incident.type,
                    "videos": incident.videos
                }
            )
    return all_incidents

token_expired={"Content-Type": "application/json","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjIsImV4cCI6MTU0NjI2MzQxMn0.aszd39bdMvIZnOTfMkHCH5tESTd1cfav06hs0Pp58ko"}

token_Invalid={"Content-Type": "application/json","token":"eyJ0eXAiOiJKV1iLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjIsImV4cCI6MTU0NjI2MzQxMn0.aszd39bdMvIZnOTfMkHCH5tESTd1cfav06hs0Pp58ko"}


def encode_token_test(userId):
    token = jwt.encode({'userId': userId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=20)},
        "secret_key")
    return token

token_signature_error={"Content-Type": "application/json","token": encode_token_test(1)}

def token_header(token):
    message = {"Content-Type": "application/json","token": token}
    return message
