import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.helpers.auth import encode_token,encode_token_test

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
"email": "manuel@ireporter.com",
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
        "userId": 3,
        "userName": "mats"
    }
}

login_user = {
    "password": "admin123",
    "email": "admin@ireporter.com"
}

invalid_login_user={
    "password": "admin",
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
            "email": "manuel@ireporter.com",
            "isAdmin": False,
            "name": "manuel manuelLastname manuelOthername",
            "phoneNumber": 256700701616,
            "userId": 2,
            "userName": "manuel"
        }
    ]
}

new_intervention = {
    "comment": "Jinja bridge needs construction",
    "createdBy": 2,
    "images": "1.jpeg",
    "locationLong": 6.66666,
    "locationLat": 7.7777,
    "type": "redflag",
    "videos": "1.gif"
}

example_create_data={"comment": "comment","images": "image name",
        "locationLat": 0.111111,"locationLong": 0.1111111,"videos": "video name"}
invalid_key_msg = "Invalid Key in data,please provide valid input data"

new_intervention_response = {
    "data": [
        {
            "id": 3,
            "message": "Created intervention record"
        }
    ],
    "status": 201
}
new_location = {
    "locationLong": 8.555555,
    "locationLat": 5.88289
}
new_comment = {"comment": "Sorry!, error information"}

new_redflag = {
"comment": "Arnold was caught stealing jack fruit in hassan's Garden",
"createdBy": 2,
"images": "1.jpeg",
"locationLong": 6.66666,
"locationLat": 7.7777,
"type": "redflag",
"videos": "1.gif"

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


new_redflag_response = {
    "data": [
        {
            "id": 3,
            "message": "Created redflag record"
        }
    ],
    "status": 201
}


error = {"status":404, "error": "Sorry, Incident Not Found"}


def get_incidents_by_type(incident_type):
    all_incidents = []

    for incident in redflag_table:
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


token_signature_error={"Content-Type": "application/json","token": encode_token_test(1)}

def token_header(token):
    message = {"Content-Type": "application/json","token": token}
    return message
