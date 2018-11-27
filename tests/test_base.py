import unittest
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
        message = "Hello Ireporter"
        self.assertEqual(data,message)



if __name__ == '__main__':
    unittest.main()
