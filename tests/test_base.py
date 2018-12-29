from flask import jsonify
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.helpers.auth import encode_token
from api.models.user_model import User


new_user = {
"email": "ematembu@ireporter.com",
"firstName": "manuel",
"lastName": "Dominic",
"otherName": "highway",
"password": "manuel123",
"phoneNumber": 256700701616,
"userName": "mats"
}


new_msg = {"status": 201,
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

new_user_response = {
    "status": 201,
    "message": "Successfully registered",
    "users": new_msg
      }

login_user = {
    "password": "admin123",
    "email": "admin@ireporter.com"
}

new_status="Resloved"

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
    "createdBy": 3,
    "images": "1.jpeg",
    "locationLong": "6.66666",
    "locationLat": "7.7777",
    "type": "redflag",
    "videos": "1.gif"

}
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
    "locationLong": "8.555555",
    "locationLat": "5.88289"
}
new_comment = {"comment": "Sorry!, error information"}

new_redflag = {
"comment": "Arnold was caught stealing jack fruit in hassan's Garden",
"createdBy": 2,
"images": "1.jpeg",
"locationLong": "6.66666",
"locationLat": "7.7777",
"type": "redflag",
"videos": "1.gif"

}
new_redflag_response = {
    "data": [
        {
            "id": 3,
            "message": "Created red-flag record"
        }
    ],
    "status": 201
}

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



def token_header(token):
    message = {"Content-Type": "application/json","token": token}
    return message
