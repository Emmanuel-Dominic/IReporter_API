import json
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from .test_base import TestBase, new_intervention, invalid_key_msg, error, example_create_data, \
    new_status, new_bad_intervention, new_error_intervention, new_comment, \
    new_error_redflag, token_header, new_bad_redflag, new_location
from api.app import app
from api.helpers.auth import encode_token


class TestIncidenterrors(TestBase):
    def test_get_specific_intervention_with_error_id(self):
        response = self.app.get('/api/v1/intervention/25', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_get_specific_redflags_with_error_id(self):
        response = self.app.get('/api/v1/red-flags/82', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_intervention_location_with_error_id(self):
        response = self.app.patch('/api/v1/intervention/25/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_redflag_location_with_error_id(self):
        response = self.app.patch('/api/v1/red-flags/12/location', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_location))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_redflag_comment_with_error_id(self):
        response = self.app.patch('/api/v1/red-flags/21/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_intervention_comment_with_error_id(self):
        response = self.app.patch('/api/v1/intervention/45/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_delete_intervention_with_error_id(self):
        response = self.app.delete('/api/v1/intervention/30', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_delete_redflag_with_error_id(self):
        response = self.app.delete('/api/v1/red-flags/35', headers=token_header(encode_token(2)))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_create_redflag_key_error(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_error_redflag))
        self.assertEqual(response.status_code, 400)
        data = response.data.decode()
        message = {"message": invalid_key_msg,
                   "example": example_create_data}
        self.assertEqual(json.loads(data)["message"], message["message"])
        self.assertEqual(json.loads(data)["example"]["comment"], message["example"]["comment"])

    def test_create_redflag_bad_error(self):
        response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_bad_redflag))
        self.assertEqual(response.status_code, 400)
        data = response.data.decode()
        message = {"message": invalid_key_msg,
                   "example": example_create_data}
        self.assertEqual(json.loads(data)["message"], message["message"])
        self.assertEqual(json.loads(data)["example"]["title"], message["example"]["title"])

    def test_create_intervention_key__error(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_error_intervention))
        self.assertEqual(response.status_code, 400)
        data = response.data.decode()
        message = {"message": invalid_key_msg,
                   "example": example_create_data}
        self.assertEqual(json.loads(data)["message"], message["message"])
        self.assertEqual(json.loads(data)["example"]["comment"], message["example"]["comment"])

    def test_create_intervention_bad__error(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
                                 data=json.dumps(new_bad_intervention))
        self.assertEqual(response.status_code, 400)
        data = response.data.decode()
        message = {"message": invalid_key_msg,
                   "example": example_create_data}
        self.assertEqual(json.loads(data), message)

    def test_create_intervention_user__error(self):
        response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(1)),
                                 data=json.dumps(new_bad_intervention))
        self.assertEqual(response.status_code, 401)
        data = response.data.decode()
        message = {"messsage": "Only Non admin can access this route"}
        self.assertEqual(json.loads(data), message)

    def test_update_intervention_status_with_error_id(self):
        response = self.app.patch('/api/v1/intervention/12/status', headers=token_header(encode_token(1)),
                                  data=json.dumps(new_status))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_redflag_status_with_error_id(self):
        response = self.app.patch('/api/v1/red-flags/10/status', headers=token_header(encode_token(1)),
                                  data=json.dumps(new_status))
        self.assertEqual(response.status_code, 404)
        data = response.data.decode()
        self.assertEqual(json.loads(data), error)

    def test_update_not_possible_comment(self):
        response = self.app.patch('/api/v1/red-flags/4/comment', headers=token_header(encode_token(2)),
                                  data=json.dumps(new_comment))
        self.assertEqual(response.status_code, 406)
        data = response.data.decode()
        message = {"status": 406, "Message": "Sorry, Update not Possible"}
        self.assertEqual(json.loads(data), message)


if __name__ == '__main__':
    unittest.main()
