import json
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from .test_base import TestBase, get_all_intervention, get_intervention, get_redflag, get_all_redflags, \
    new_intervention, error, new_location, new_status, \
    new_bad_intervention, new_error_intervention, \
    new_comment, intervention_status_response, new_error_redflag, \
    new_intervention_response, redflag_status_response, new_redflag, \
    new_redflag_response, token_header
from api.helpers.auth import encode_token


class TestIncindent(TestBase):
    def test_index(self):
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {
            'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}
        self.assertEqual(json.loads(data), message)

    def test_get_all_redflags(self):
        response = self.app.get('/api/v1/red-flags', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        self.assertEqual(len(json.loads(data)), len(get_all_redflags))
        self.assertEqual(json.loads(data)["data"][0]["comment"], get_all_redflags["data"][0]["comment"])
        self.assertEqual(json.loads(data)["status"], get_all_redflags["status"])
        self.assertEqual(json.loads(data)["data"][-1]["title"], get_all_redflags["data"][-1]["title"])

    def test_get_all_intervention(self):
        response = self.app.get('/api/v1/intervention', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        self.assertEqual(len(json.loads(data)), len(get_all_intervention))
        self.assertEqual(json.loads(data)["data"][-1]["comment"], get_all_intervention["data"][-1]["comment"])
        self.assertEqual(json.loads(data)["status"], get_all_intervention["status"])
        self.assertEqual(json.loads(data)["data"][0]["title"], get_all_intervention["data"][0]["title"])

    def test_get_specific_intervention(self):
        response = self.app.get('/api/v1/intervention/5', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        self.assertEqual(len(json.loads(data)), len(get_intervention))
        self.assertEqual(json.loads(data)["data"]["comment"], get_intervention["data"]["comment"])

    def test_get_specific_redflags(self):
        response = self.app.get('/api/v1/red-flags/1', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        self.assertEqual(len(json.loads(data)), len(get_redflag))
        self.assertEqual(json.loads(data)["data"]["title"], get_redflag["data"]["title"])

    def test_update_intervention_location(self):
        response = self.app.patch('/api/v1/intervention/6/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {"status": 200, "data": [[{"incident_id": 6}],
                                           {"message": "Intervention location successfully Updated"}]}
        self.assertEqual(json.loads(data), message)

    def test_update_redflag_location(self):
        response = self.app.patch('/api/v1/red-flags/2/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {"data": [[{"incident_id": 2}],
                            {"message": "Redflag location successfully Updated"}],
                   "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_update_redflag_comment(self):
        response = self.app.patch('/api/v1/red-flags/2/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {"data": [{"incident_id": 2},
                            {"message": "Redflag comment successfully Updated"}], "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_update_intervention_comment(self):
        response = self.app.patch('/api/v1/intervention/6/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {"data": [{"incident_id": 6},
                            {"message": "Intervention comment successfully Updated"}], "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_create_redflag(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)), data=json.dumps(new_redflag))
        data = response.data.decode()
        self.assertTrue(json.loads(data), new_redflag_response)


    def test_create_intervention(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_intervention))
        data = response.data.decode()
        self.assertTrue(json.loads(data), new_intervention_response)



    def test_delete_intervention(self):
        response = self.app.delete('/api/v1/intervention/7', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {"data": [{"incident_id": 7},
                            {"message": "Intervention successfully Deleted"}], "status": 200}
        self.assertEqual(json.loads(data), message)

    def test_delete_redflag(self):
        response = self.app.delete('/api/v1/red-flags/3', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {"data": [{"incident_id": 3},
                            {"message": "Redflag successfully Deleted"}], "status": 200}
        self.assertEqual(json.loads(data), message)


    def test_update_intervention_status(self):
        response = self.app.patch('/api/v1/intervention/5/status', headers=token_header(encode_token(1)),
                                  data=json.dumps(new_status))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        self.assertEqual(json.loads(data), intervention_status_response)


    def test_update_redflag_status(self):
        response = self.app.patch('/api/v1/red-flags/1/status', headers=token_header(encode_token(1)),\
                                          data=json.dumps(new_status))
        self.assertEqual(response.status_code,200)
        data = response.data.decode()
        self.assertEqual(json.loads(data), redflag_status_response)


if __name__ == '__main__':
    unittest.main()
