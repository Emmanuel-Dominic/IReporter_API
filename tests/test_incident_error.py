import json
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from api.models.incident_model import intervention_table,redflag_table
from .test_base import new_intervention,error,new_location,bad_message,new_status,new_bad_intervention,new_error_intervention,new_comment,new_error_redflag,new_intervention_response,token_header,new_bad_redflag
from api.app import app
from .test_base import new_redflag,new_location,new_comment,new_redflag_response,token_header
from api.helpers.auth import encode_token
from api.helpers.incidenthelper import get_incidents_by_type,get_incidents_by_type_id



class TestIntervention(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.assertFalse(app.config['SECRET_KEY'] is 'softwareDeveloper.Manuel@secret_key/mats.com')

    def test_index(self):
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {
            'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}
        self.assertEqual(json.loads(data), message)


    def test_get_all_intervention(self):
        response = self.app.get('/api/v1/intervention', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        message = {"data": get_incidents_by_type("intervention"), "status": 200}
        self.assertTrue(json.loads(data), message)


    def test_get_specific_intervention_with_error_id(self):
        response = self.app.get('/api/v1/intervention/25', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_get_specific_redflags_with_error_id(self):
        response = self.app.get('/api/v1/red-flags/82', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_update_intervention_location_with_error_id(self):
        response = self.app.patch('/api/v1/intervention/25/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_update_redflag_location_with_error_id(self):
        response = self.app.patch('/api/v1/red-flags/12/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_update_redflag_comment_with_error_id(self):
        response = self.app.patch('/api/v1/red-flags/21/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_update_intervention_comment_with_error_id(self):
        response = self.app.patch('/api/v1/intervention/45/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_delete_intervention_with_error_id(self):
        response = self.app.delete('/api/v1/intervention/30', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_delete_redflag_with_error_id(self):
        response = self.app.delete('/api/v1/red-flags/5', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_create_redflag_key_error(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)), data=json.dumps(new_error_redflag))
        self.assertEqual(response.status_code,400)
        data = response.data.decode()
        message={"Required format": {
                "comment": "RedFlag comment",
                "images": "image name",
                "locationLong": "0.0000",
                "locationLat": "0.00000",
                "videos": "video name"
            }}
        self.assertEqual(json.loads(data), message)

    def test_create_redflag_bad_error(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)), data=json.dumps(new_bad_redflag))
        self.assertEqual(response.status_code,400)
        data = response.data.decode()
        self.assertEqual(json.loads(data), bad_message)


    def test_create_intervention_key__error(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_error_intervention))
        self.assertEqual(response.status_code,400)
        data = response.data.decode()
        message={"Required format": {
                "comment": "Intervention comment",
                "images": "image name",
                "locationLong": 0.0576,
                "locationLat": 0.001516,
                "videos": "video name"
            }}
        self.assertEqual(json.loads(data), message)

    def test_create_intervention_bad__error(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_bad_intervention))
        self.assertEqual(response.status_code,400)
        data = response.data.decode()
        self.assertEqual(json.loads(data), bad_message)

    def test_create_intervention_user__error(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(1)),
                                 data=json.dumps(new_bad_intervention))
        self.assertEqual(response.status_code,401)
        data = response.data.decode()
        message={"messsage": "Only Non admin can access this route"}
        self.assertEqual(json.loads(data), message)


    def test_update_intervention_status_with_error_id(self):
        response = self.app.patch('/api/v1/intervention/12/status', headers=token_header(encode_token(1)),
                                  data=json.dumps(new_status))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)


    def test_update_redflag_status_with_error_id(self):
        response = self.app.patch('/api/v1/red-flags/10/status', headers=token_header(encode_token(1)),
                                  data=json.dumps(new_status))
        self.assertEqual(response.status_code,404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_not_possible_comment(self):
        response = self.app.patch('/api/v1/intervention/1/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code,406)
        data = response.data.decode()
        message={"status":406, "error": "Sorry, Update not Possible"}
        self.assertEqual(json.loads(data), message)

if __name__ == '__main__':
    unittest.main()
