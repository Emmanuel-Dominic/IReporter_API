import json
import unittest
import datetime
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.views.redflag_view import redflag_bp
from api import app

new_redflag= {
    "comment": "Arnold was caught stealing jack fruit in hassan's Garden",
    "createdBy": 2,
    "images": "1.jpeg",
    "locationLong": "6.66666" ,
    "locationLat":"7.7777",
    "type": "redflag",
    "videos": "1.gif"

 }
new_redflag_response = {
    "data": [
        {
            "id": 2,
            "message": "Created red-flag record"
        }
    ],
    "status": 200
}
new_location ={
    "locationLong": "8.555555",
    "locationLat": "5.88289"
}
new_comment = {"comment": "Sorry!, error information"}
def get_incidents_by_type(incident_type):
    all_incidents =  []

    for incident in incidents_db:
        if incident.type ==incident_type:
            all_incidents.append(
            {
                "comment":incident.comment,
                "createdBy":incident.createdBy,
                "createdOn":incident.createdOn,
                "images":incident.images,
                "incidentId":incident.incidentId,
                "location": " ".join([incident.locationLong,',', incident.locationLat]),
                "status":incident.status,
                "type":incident.type,
                "videos":incident.videos
            }
            )
    return all_incidents

class TestRedflag(unittest.TestCase):

    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.client = app.test_client()


    def test_index(self):
        response = self.client.get('/api/v1/')
        data = response.data.decode()
        message = {'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}
        self.assertEqual(json.loads(data),message)

    def test_get_all_redflags(self):
        response = self.client.get('/api/v1/red-flags')
        data = response.data.decode()
        message = {"data":get_incidents_by_type("red-flag"), "status": 200}
        self.assertEqual(len(json.loads(data)),len(message))


    def test_get_specific_redflags(self):
        response = self.client.get('/api/v1/red-flags/1')
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
        self.assertEqual(json.loads(data),message)


    def test_create_redflag(self):
        response = self.client.post('/api/v1/red-flags', content_type="application/json",data=json.dumps(new_redflag))
        data = response.data.decode()
        self.assertEqual(json.loads(data),new_redflag_response)

    def test_update_redflag_location(self):
        response = self.client.patch('/api/v1/red-flags/1/location', content_type="application/json",data=json.dumps(new_location))
        data = response.data.decode()
        message = {"data": [{"id": 1, "message": "Updated red-flag record's location"}],
            "status": 200}
        self.assertEqual(json.loads(data),message)


    def test_update_redflag_comment(self):
        response = self.client.patch('/api/v1/red-flags/1/comment', content_type="application/json",data=json.dumps(new_comment))
        data = response.data.decode()
        message = {"data": [{"id": 1, "message": "Updated red-flag record's comment"}],
            "status": 200}
        self.assertEqual(json.loads(data),message)

    def test_delete_redflag(self):
        response = self.client.delete('/api/v1/red-flags/2')
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "red-flag record has been deleted"}],
            "status": 200}
        self.assertEqual(json.loads(data),message)


if __name__ == '__main__':
    unittest.main()
