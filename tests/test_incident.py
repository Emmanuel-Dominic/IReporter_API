import json
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.models.incident_model import redflag_table,intervention_table
from api.app import app

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
            "id": 4,
            "message": "Created red-flag record"
        }
    ],
    "status": 200
}
new_location = {
    "locationLong": "8.555555",
    "locationLat": "5.88289"
}
new_comment = {"comment": "Sorry!, error information"}

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
            "id": 4,
            "message": "Created intervention record"
        }
    ],
    "status": 200
}
new_location = {
    "locationLong": "8.555555",
    "locationLat": "5.88289"
}
new_comment = {"comment": "Sorry!, error information"}



class TestRedflag(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # def test_index(self):
    #     response = self.app.get('/api/v1/auth/')
    #     data = response.data.decode()
    #     message = {
    #         'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}
    #     self.assertEqual(json.loads(data), message)

    def test_get_all_redflags(self):
        response = self.app.get('/api/v1/auth/red-flags')
        data = response.data.decode()
        message = {"data": redflag_table, "status": 200}
        self.assertEqual(len(json.loads(data)), len(message))

    def test_get_specific_redflags(self):
        response = self.app.get('/api/v1/auth/red-flags/1')
        data = response.data.decode()
        message = {
            "data": {
                "comment": "Arnold was caught stealing jack fruit in hassan's Garden",
                "createdBy": 2,
                "createdOn": "Fri, 30 Nov 2018 13:09:32 GMT",
                "images": "1.jpeg",
                "incidentId": 1,
                "location": "0.33737 , 5.38974",
                "status": "draft",
                "type": "red-flag",
                "videos": "1.gif"
            },
            "status": 200
        }
        self.assertEqual(json.loads(data), message)

    def test_create_redflag(self):
        response = self.app.post('/api/v1/auth/red-flags', content_type="application/json", data=json.dumps(new_redflag))
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_redflag_response)

    def test_update_redflag_location(self):
        response = self.app.patch('/api/v1/auth/red-flags/1/location', content_type="application/json",
                                  data=json.dumps(new_location))
        data = response.data.decode()
        message = {"data": [{"id": 1, "message": "Updated red-flag record's location"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_update_redflag_comment(self):
        response = self.app.patch('/api/v1/auth/red-flags/1/comment', content_type="application/json",
                                  data=json.dumps(new_comment))
        data = response.data.decode()
        message = {"data": [{"id": 1, "message": "Updated red-flag record's comment"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_delete_redflag(self):
        response = self.app.delete('/api/v1/auth/red-flags/1')
        data = response.data.decode()
        message = {"data": [{"id": 1, "message": "red-flag record has been deleted"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)


    def test_get_all_intervention(self):
        response = self.app.get('/api/v1/auth/intervention')
        data = response.data.decode()
        message = {"data": intervention_table, "status": 200}
        self.assertEqual(len(json.loads(data)), len(message))

    def test_get_specific_intervention(self):
        response = self.app.get('/api/v1/auth/intervention/1')
        data = response.data.decode()
        message = {
            "data": {
                "comment": "Mbale highway needs construction",
                "createdBy": 2,
                "createdOn": "Fri, 30 Nov 2018 13:09:32 GMT",
                "images": "1.jpeg",
                "incidentId": 1,
                "location": "0.33737 , 5.38974",
                "status": "draft",
                "type": "intervention",
                "videos": "1.gif"
            },
            "status": 200
        }
        self.assertEqual(json.loads(data), message)

    def test_create_intervention(self):
        response = self.app.post('/api/v1/auth/intervention', content_type="application/json",
                                 data=json.dumps(new_intervention))
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_intervention_response)

    def test_update_intervention_location(self):
        response = self.app.patch('/api/v1/auth/intervention/2/location', content_type="application/json",
                                  data=json.dumps(new_location))
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "Updated intervention record's location"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_update_intervention_comment(self):
        response = self.app.patch('/api/v1/auth/intervention/2/comment', content_type="application/json",
                                  data=json.dumps(new_comment))
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "Updated intervention record's comment"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_delete_intervention(self):
        response = self.app.delete('/api/v1/auth/intervention/4')
        data = response.data.decode()
        message = {"data": [{"id": 4, "message": "intervention record has been deleted"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)


if __name__ == '__main__':
    unittest.main()
