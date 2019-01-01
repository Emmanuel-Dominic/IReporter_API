# import json
# import unittest
# import os
# import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
# from api.views.redflag_view import redflag_table
# from .test_base import new_redflag,new_location,new_comment,new_redflag_response,token_header
# from api.app import app
# from api.helpers.auth import encode_token



# class TestRedflag(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['DEBUG'] = True
#         self.app = app.test_client()
#         self.assertFalse(app.config['SECRET_KEY'] is 'softwareDeveloper.Manuel@secret_key/mats.com')


#     def test_index(self):
#         response = self.app.get('/api/v1/')
#         # self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {
#             'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}
#         self.assertEqual(json.loads(data), message)

#     def test_get_all_redflags(self):
#         response = self.app.get('/api/v1/red-flags', headers=token_header(encode_token(2)))
#         # self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": redflag_table, "status": 200}
#         self.assertEqual(len(json.loads(data)), len(message))

#     def test_get_specific_redflags(self):
#         response = self.app.get('/api/v1/red-flags/2', headers=token_header(encode_token(2)))
#         # self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message ={
#                 "data": {
#                     "comment": "james was caught idle and disorderly",
#                     "createdBy": 2,
#                     "createdOn": "Fri, 30 Nov 2018 12:09:32 GMT",
#                     "images": "1.jpeg",
#                     "incidentId": 2,
#                     "locationLat": 5.38974,
#                     "locationLong": 0.33737,
#                     "status": "draft",
#                     "type": "red-flag",
#                     "videos": "1.gif"
#                 },
#                 "status": 200
#             }
#         self.assertEqual(json.loads(data), message)

#     def test_create_redflag(self):
#         response = self.app.post('/api/v1/red-flags', headers=token_header(encode_token(2)), data=json.dumps(new_redflag))
#         self.assertEqual(response.status_code,201)
#         data = response.data.decode()
#         self.assertEqual(json.loads(data), new_redflag_response)

#     def test_update_redflag_location(self):
#         response = self.app.patch('/api/v1/red-flags/2/location', headers=token_header(encode_token(2)),
#                                   data=json.dumps(new_location))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": [{"id": 2, "message": "Updated red-flag record's location"}],
#                    "status": 200}
#         self.assertEqual(json.loads(data), message)

#     def test_update_redflag_comment(self):
#         response = self.app.patch('/api/v1/red-flags/2/comment', headers=token_header(encode_token(2)),
#                                   data=json.dumps(new_comment))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": [{"id": 2, "message": "Updated red-flag record's comment"}],
#                    "status": 200}
#         self.assertEqual(json.loads(data), message)

#     def test_delete_redflag(self):
#         response = self.app.delete('/api/v1/red-flags/2', headers=token_header(encode_token(2)))
#         self.assertEqual(response.status_code,200)
#         data = response.data.decode()
#         message = {"data": [{"id": 2, "message": "red-flag record has been deleted"}],
#                    "status": 200}
#         self.assertEqual(json.loads(data), message)



# if __name__ == '__main__':
#     unittest.main()
