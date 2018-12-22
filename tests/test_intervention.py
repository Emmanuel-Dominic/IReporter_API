import json
import unittest
# import os
# import sys
#
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from views.intervention_view import intervention_table
from app import app

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


def get_incidents_by_type(incident_type):
    all_incidents = []

    for incident in intervention_table:
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


class TestIntervention(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_get_all_intervention(self):
        response = self.app.get('/api/v1/intervention')
        data = response.data.decode()
        message = {"data": get_incidents_by_type("intervention"), "status": 200}
        self.assertEqual(len(json.loads(data)), len(message))

    def test_get_specific_intervention(self):
        response = self.app.get('/api/v1/intervention/1')
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
        response = self.app.post('/api/v1/intervention', content_type="application/json",
                                 data=json.dumps(new_intervention))
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_intervention_response)

    def test_update_intervention_location(self):
        response = self.app.patch('/api/v1/intervention/2/location', content_type="application/json",
                                  data=json.dumps(new_location))
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "Updated intervention record's location"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_update_intervention_comment(self):
        response = self.app.patch('/api/v1/intervention/2/comment', content_type="application/json",
                                  data=json.dumps(new_comment))
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "Updated intervention record's comment"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_delete_intervention(self):
        response = self.app.delete('/api/v1/intervention/4')
        data = response.data.decode()
        message = {"data": [{"id": 4, "message": "intervention record has been deleted"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)


if __name__ == '__main__':
    unittest.main()
