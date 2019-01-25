import unittest
import datetime
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.app import app
from api.helpers.auth import encode_token, encode_token_test
from api.models.database_model import DatabaseConnection
from werkzeug.security import check_password_hash


class TestBase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.db = DatabaseConnection()
        self.db.cursor.execute(open('work.sql', 'r').read())

new_user = {
    "email": "ematembu3@gmail.com",
    "firstName": "Emmanuel",
    "isadmin": False,
    "joinning": "Thu, 10 Jan 2019 04:01:14 GMT",
    "lastName": "Matembu",
    "otherName": "Dominic",
    "password": "pbkdf2:sha256:50000$sQueRoWd$816cacdef85cee03292df7cb84af19f9a0fb10a547d31178d9fccdf55fe80698",
    "phoneNumber": 256700701616,
    "user_id": 3,
    "userName": "Manuel"
}

new_user_response = {"status": 201, "message": "Successfully registered",
                     "data": {
                         "phone_number": "256700701616",
                         "email": "ematembu2@gmail.com",
                         "first_name": "Emmanuel",
                         "isadmin": False,
                         "joinning": "Thu, 10 Jan 2019 04:01:14 GMT",
                         "last_name": "Matembu",
                         "other_name": "Dominic",
                         "user_id": 3,
                         "user_name": "Manuel"
                     }, "token": encode_token(3)
                     }

login_user = {
    "email": "ireporterManuelDominic@gmail.com",
    "password": "admin123"
}

login_user_response = {
    "message": "Successfully logged In",
    "token": encode_token(1)
}

all_users_response = {
    "data": [
        [
            {
                "email": "ematembu2@gmail.com",
                "first_name": "manuel",
                "isadmin": False,
                "joinning": "Thu, 10 Jan 2019 04:01:14 GMT",
                "last_name": "manuellast_Name",
                "other_name": "manuelother_Name",
                "passwd": "pbkdf2:sha256:50000$kEBD7Z97$97db32267f5d0956994c5db567ffda9f45cd6f136a7e2d0f9029f3d68b882b1c",
                "phone_number": "256700701616",
                "user_id": 2,
                "user_name": "manuel"
            }
        ]
    ],
    "status": 200
}

new_intervention = {
    "title": "intervention",
    "comment": "Jinja bridge needs construction",
    "createdBy": 2,
    "incident_type": "intervention",
    "created_On": "Thu, 10 Jan 2019 04:01:14 GMT",
    "images": "1.jpeg",
    "longtitude": 6.66666,
    "latitude": 7.7777,
    "videos": "1.gif"
}

new_intervention_response = {
    "Data": [
        {
            "incident_id": 8
        },
        {
            "message": "Intervention Successfully created"
        }
    ],
    "status": 201
}

new_intervention_response["Data"][1] = {"message": "Intervention Successfully created"}

new_redflag = {
    "title": "Theft",
    "createdBy": 2,
    "comment": "james idle and disorderly",
    "incident_type": "redflag",
    "created_On": "Thu, 10 Jan 2019 04:01:14 GMT",
    "images": "1.jpeg",
    "latitude": 5.38974,
    "longtitude": 0.33737,
    "videos": "1.gif"
}

new_redflag_response = {
    "Data": [
        {
            "incident_id": int
        },
        {
            "message": "Redflag Successfully created"
        }
    ],
    "status": 201
}

new_redflag_response["Data"][1] = {"message": "Redflag Successfully created"}

get_all_redflags = {
    "data": [
        {
            "comment": "Arnold stole hassan phone and laptop from his car",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 1,
            "incident_type": "redflag",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Theift",
            "videos": "1.gif"
        },
        {
            "comment": "Every night at malamba boarders, people smuggle kenya rice into the country",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 2,
            "incident_type": "redflag",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Smuggling",
            "videos": "1.gif"
        },
        {
            "comment": "Timothy raped Jane last night at 11pm after breaking into her apartment",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 3,
            "incident_type": "redflag",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "Rejected",
            "title": "Rape",
            "videos": "1.gif"
        },
        {
            "comment": "Hadrico raped lona last month at 11pm after breaking into her apartment",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 4,
            "incident_type": "redflag",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "Rejected",
            "title": "Rape",
            "videos": "1.gif"
        }
    ],
    "status": 200
}

get_redflag = {
    "data":
        {
            "comment": "Arnold stole hassan phone and laptop from his car",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 1,
            "incident_type": "redflag",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Theift",
            "videos": "1.gif"
        }
    ,
    "status": 200
}

get_all_intervention = {
    "data": [
        {
            "comment": "Mbale highway broken down after a previous track accident last month amonth ",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 5,
            "incident_type": "intervention",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Road Breakdown",
            "videos": "1.gif"
        },
        {
            "comment": "Mbarara medical facilities lack proper medication and labour ward services",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 6,
            "incident_type": "intervention",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Incoprate hospital services",
            "videos": "1.gif"
        },
        {
            "comment": "Jinja bridge needs replacement because it is past its deadline date",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 7,
            "incident_type": "intervention",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Bridge construction",
            "videos": "1.gif"
        }
    ],
    "status": 200
}

get_intervention = {
    "data":
        {
            "comment": "Mbale highway broken down after a previous track accident last month amonth ",
            "created_by": 2,
            "created_on": "Thu, 10 Jan 2019 04:01:14 GMT",
            "images": "1.jpeg",
            "incident_id": 5,
            "incident_type": "intervention",
            "latitude": 5.38974,
            "longtitude": 0.33737,
            "status_": "draft",
            "title": "Road Breakdown",
            "videos": "1.gif"
        }
    ,
    "status": 200
}

new_comment = {"comment": "Just testing comment"}

new_comment_response = {
    "Data": [
        {
            "incident_id": 1
        },
        {
            "message": "intervention comment successfully Updated"
        }
    ],
    "status": 200
}

new_location = {
    "latitude": 25.5585,
    "longtitude": 55.6866
}

new_location_response = {
    "Data": [
        [
            {
                "incident_id": 1
            }
        ],
        {
            "message": "intervention location successfully Updated"
        }
    ],
    "status": 200
}

new_status = {
    "status": "Resolved"
}

redflag_status_response = {
    "Data": [
        {
            "incident_id": 1
        },
        {
            "message": "Redflag status successfully Updated"
        }
    ],
    "status": 200
}

intervention_status_response = {
    "Data": [
        {
            "incident_id": 5
        },
        {
            "message": "Intervention status successfully Updated"
        }
    ],
    "status": 200
}

new_user_error_mail = {
    "email": "ematembu2@gmail.com",
    "firstName": "manuel",
    "lastName": "Dominic",
    "otherName": "highway",
    "password": "manuel123",
    "phoneNumber": 256700701616,
    "userName": "mats"
}

invalid_login_user = {
    "password": "admin123",
    "email": "admin@ireporter.com"
}

new_bad_redflag = {}

new_bad_intervention = {}

new_error_redflag = {
    "titles": "redflag",
    "comment": "Jinja bridge needs construction",
    "createdBy": 2,
    "incident_type": "redflag",
    "created_On": "Thu, 10 Jan 2019 04:01:14 GMT",
    "images": "1.jpeg",
    "longtitude": 6.66666,
    "latitude": 7.7777,
    "videos": "1.gif"
}

new_error_intervention = {
    "title": "intervention",
    "comments": "Jinja bridge needs construction",
    "createdBy": 2,
    "incident_type": "intervention",
    "created_On": "Thu, 10 Jan 2019 04:01:14 GMT",
    "images": "1.jpeg",
    "longtitude": 6.66666,
    "latitude": 7.7777,
    "videos": "1.gif"
}

error = {"status": 404, "error": "Sorry, Incident Not Found"}

token_expired = {"Content-Type": "application/json",
                 "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsImV4cCI6MTEzNjA2ODczMn0.jnahXxePeXcJEJM4F8iQgNVMVQquE1Mh64XV26juvs8"}

token_Invalid = {"Content-Type": "application/json",
                 "token": "eyJ0eXAiOiJKV1iLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjIsImV4cCI6MTU0NjI2MzQxMn0.aszd39bdMvIZnOTfMkHCH5tESTd1cfav06hs0Pp58ko"}

token_signature_error = {"Content-Type": "application/json", "token": encode_token_test(1)}

example_create_data = {
    "title": "title",
    "comment": "comment",
    "images": "1.jpeg",
    "longtitude": 6.66666,
    "latitude": 7.7777,
    "videos": "1.gif"
}
invalid_key_msg = "Invalid Key in data,please provide valid input data"


def token_header(token):
    message = {"Content-Type": "application/json", "token": token}
    return message
