# import json
# import unittest
# import os
# import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
# from api.views.intervention_view import intervention_table
# from .test_base import new_intervention,new_location,new_status,new_comment,new_intervention_response,token_header
# from api.app import app
# from api.helpers.auth import encode_token



# class TestIntervention(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['DEBUG'] = True
#         self.app = app.test_client()
#         self.assertFalse(app.config['SECRET_KEY'] is 'softwareDeveloper.Manuel@secret_key/mats.com')


#     def test_get_all_intervention(self):
#         response = self.app.get('/api/v1/intervention', headers=token_header(encode_token(2)))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": intervention_table, "status": 401}
#         self.assertEqual(len(json.loads(data)), len(message))

#     def test_get_specific_intervention(self):
#         response = self.app.get('/api/v1/intervention/1', headers=token_header(encode_token(2)))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": {
#                         "comment": "Mbale highway needs construction",
#                         "createdBy": 2,
#                         "createdOn": "Fri, 30 Nov 2018 13:09:32 GMT",
#                         "images": "1.jpeg",
#                         "incidentId": 1,
#                         "locationLat": 5.38974,
#                         "locationLong": 0.33737,
#                         "status": "draft",
#                         "type": "intervention",
#                         "videos": "1.gif"
#                     },
#                     "status": 200
#                 }
#         self.assertEqual(json.loads(data), message)

#     def test_create_intervention(self):
#         response = self.app.post('/api/v1/intervention', headers=token_header(encode_token(2)),
#                                  data=json.dumps(new_intervention))
#         self.assertEqual(response.status_code,201)
#         data = response.data.decode()
#         self.assertEqual(json.loads(data), new_intervention_response)

#     def test_update_intervention_location(self):
#         response = self.app.patch('/api/v1/intervention/1/location', headers=token_header(encode_token(2)),
#                                   data=json.dumps(new_location))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": [{"id": 1, "message": "Updated intervention record's location"}],
#                    "status": 200}
#         self.assertEqual(json.loads(data), message)

#     def test_update_intervention_comment(self):
#         response = self.app.patch('/api/v1/intervention/1/comment', headers=token_header(encode_token(2)),
#                                   data=json.dumps(new_comment))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": [{"id": 1, "message": "Updated intervention record's comment"}],
#                    "status": 200}
#         self.assertEqual(json.loads(data), message)

#     def test_delete_intervention(self):
#         response = self.app.delete('/api/v1/intervention/2', headers=token_header(encode_token(2)))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": [{"id": 2, "message": "intervention record has been deleted"}],
#                    "status": 200}
#         self.assertEqual(json.loads(data), message)


#     # def test_update_intervention_status(self):
#     #     response = self.app.patch('/api/v1/intervention/1/status', headers=token_header(encode_token(1)),
#     #                               data=json.dumps(new_status))
#     #     self.assertEqual(response.status_code,200)
#     #     data = response.data.decode()
#     #     message = {"data": [{"id": 1, "message": "Updated intervention record's status"}],
#     #                "status": 200}
#     #     self.assertEqual(json.loads(data), message)

# if __name__ == '__main__':
#     unittest.main()
