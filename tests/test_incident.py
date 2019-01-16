from api.helpers.auth import encode_token
from api.helpers.incidenthelper import get_incidents_by_type
from .test_base import TestBase,new_intervention,new_intervention1,new_location,new_status,\
                        new_comment,new_redflag1,\
                        new_intervention_response,new_intervention1_response,new_redflag,\
                        new_redflag_response,new_redflag1_response,token_header
import json
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


class TestIntervention(TestBase):
    def test_index(self):
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {
            'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}
        self.assertEqual(json.loads(data), message)


    def test_create_redflag(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)),
                                     data=json.dumps(new_redflag))
        self.assertEqual(response.status_code,201)
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_redflag_response)


    def test_create_intervention(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_intervention))
        self.assertEqual(response.status_code,201)
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_intervention_response)

    def test_create_more_redflag(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)),
                                     data=json.dumps(new_redflag1))
        self.assertEqual(response.status_code,201)
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_redflag1_response)


    def test_create_more_intervention(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_intervention1))
        self.assertEqual(response.status_code,201)
        data = response.data.decode()
        self.assertEqual(json.loads(data), new_intervention1_response)



    def test_get_all_redflags(self):
        response = self.app.get('/api/v1/red-flags', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": get_incidents_by_type("redflag"), "status": 200}
        self.assertTrue(json.loads(data), message)

    def test_get_all_intervention(self):
        response = self.app.get('/api/v1/intervention', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": get_incidents_by_type("intervention"), "status": 200}
        self.assertTrue(json.loads(data), message)

    def test_get_specific_intervention(self):
        response = self.app.get('/api/v1/intervention/2', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": {
                    "comment": "Mbarara highway needs construction",
                    "createdBy": 2,
                    "createdOn": "Fri, 30 Nov 2018 12:09:32 GMT",
                    "images": "1.jpeg",
                    "incidentId": 2,
                    "locationLat": 5.38974,
                    "locationLong": 0.33737,
                    "status": "draft",
                    "type": "intervention",
                    "videos": "1.gif"
                },
                "status": 200
            }
        self.assertEqual(json.loads(data)["data"]["comment"], message["data"]["comment"])
        self.assertEqual(json.loads(data)["data"]["createdBy"], message["data"]["createdBy"])
        self.assertEqual(json.loads(data)["data"]["locationLong"], message["data"]["locationLong"])
        self.assertEqual(json.loads(data)["data"]["locationLat"], message["data"]["locationLat"])
        self.assertEqual(json.loads(data)["data"]["type"], message["data"]["type"])


    def test_get_specific_redflags(self):
        response = self.app.get('/api/v1/red-flags/2', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message =[
                {"data": { "comment": "james was caught idle and disorderly",
                            "createdBy": 2,
                            "createdOn": "Fri, 30 Nov 2018 12:09:32 GMT",
                            "images": "1.jpeg",
                            "incidentId": 2,
                            "locationLat": 5.38974,
                            "locationLong": 0.33737,
                            "status": "draft",
                            "type": "red-flag",
                            "videos": "1.gif"
                        }
                },
                {
                    "status": 200
                }
            ]

        self.assertEqual(json.loads(data)[0]["data"]["comment"], message[0]["data"]["comment"])
        self.assertEqual(json.loads(data)[0]["data"]["createdBy"], message[0]["data"]["createdBy"])
        self.assertEqual(json.loads(data)[0]["data"]["locationLong"], message[0]["data"]["locationLong"])
        self.assertEqual(json.loads(data)[0]["data"]["locationLat"], message[0]["data"]["locationLat"])
        self.assertEqual(json.loads(data)[0]["data"]["type"], message[0]["data"]["type"])


    def test_update_intervention_location(self):
        response = self.app.patch('/api/v1/intervention/2/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"status": 200,"data": {"id": 2, "message": "Updated intervention record's location"}}
        self.assertEqual(json.loads(data), message)

 
    def test_update_redflag_location(self):
        response = self.app.patch('/api/v1/red-flags/2/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": {"id": 2, "message": "Updated redflag record's location"},
                   "status": 200}
        self.assertEqual(json.loads(data), message)


    def test_update_redflag_comment(self):
        response = self.app.patch('/api/v1/red-flags/2/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "Updated redflag record's comment"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)


    def test_update_intervention_comment(self):
        response = self.app.patch('/api/v1/intervention/2/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": {"id": 2, "message": "Updated intervention record's comment"},
                   "status": 200}
        self.assertEqual(json.loads(data), message)

 
    def test_delete_intervention(self):
        response = self.app.delete('/api/v1/intervention/1', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": {"id": 1, "message": "intervention record has been deleted"},
                   "status": 200}
        self.assertEqual(json.loads(data), message)


    def test_delete_redflag(self):
        response = self.app.delete('/api/v1/red-flags/1', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": {"id": 1, "message": "redflag record has been deleted"},
                   "status": 200}
        self.assertEqual(json.loads(data), message)

 
    def test_update_intervention_status(self):
        response = self.app.patch('/api/v1/intervention/2/status', headers=token_header(encode_token(1)),
                                  data=json.dumps(new_status))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": [{"id": 2, "message": "Updated intervention record's status"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)


    def test_update_redflag_status(self):
        response = self.app.patch('/api/v1/red-flags/2/status', headers=token_header(encode_token(1)),\
                                          data=json.dumps(new_status))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": {"id": 2, "message": "Updated redflag record's status"},
                   "status": 200}
        self.assertEqual(json.loads(data), message)

if __name__ == '__main__':
    unittest.main()