from flask import json
import unittest
import datetime
from IReporter_API.app.app import app



class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.client = app.test_client()


    def test_index(self):
        response = self.client.get('/')
        data = response.data.decode()
        message = {"Message":"Hello Ireporter"}
        self.assertEqual(json.loads(data),message)

    # def test_get_all_redflags(self):
    #     response = self.client.get('api/v1/redflags')
    #     data = response.data.decode()
    #     message = {"data": [
    #         {
    #         "comment": "Arnold was caught stealing jack fruit in hassan's Garden",
    #         "createdBy": 2,
    #         "createdOn": datetime.datetime.now(),
    #         "images": "1.jpeg",
    #         "incidentId": 1,
    #         "location": "0.39737 , 9.38974",
    #         "status": "draft",
    #         "type": "redflag",
    #         "videos": "1.gif"
    #         },
    #         {
    #         "comment": "Hussien knocked moses's cow along masaka road, 'he was drank'",
    #         "createdBy": 2,
    #         "createdOn": datetime.datetime.now(),
    #         "images": "3.jpeg",
    #         "incidentId": 3,
    #         "location": "0.39737 , 9.38974",
    #         "status": "draft",
    #         "type": "redflag",
    #         "videos": "3.gif"
    #         }
    #         ],
    #         "status": 200
    #         },
    #     self.assertEqual(data,message)

if __name__ == '__main__':
    unittest.main()
