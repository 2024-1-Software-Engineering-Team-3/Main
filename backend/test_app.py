import unittest
from app import create_app
from models import *


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.from_object('config.TestConfig')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_register_user(self):
        response = self.client.post('/Login/signup', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('회원가입이 성공적으로 완료되었습니다.', response.get_json()['Response'])

    def test_login_user(self):
        self.test_register_user()
        response = self.client.post('/Login/login', json={
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())
        self.assertIn('testuser@example.com',
                      response.get_json()['user_info']['email'])
        self.assertIn('testuser', response.get_json()['user_info']['username'])

    def test_create_recruiting(self):
        self.test_login_user()
        response = self.client.post('/Recruitment/upload', json={
            'title': 'New Study Group',
            'description': 'A new study group for advanced topics.',
            'membercount': 10,
            'duration': '3 months',
            'place': 'Room 303',
            'type': 'study'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Recruting data가 성공적으로 생성되었습니다.',
                      response.get_json()['Response'])

    def test_join_recruitment(self):
        self.test_create_recruiting()
        response = self.client.post('/Recruitment/join', json={
            'user_id': 1,
            'recruitment_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("성공적으로 리크루먼트에 가입했습니다.", response.get_json()['Response'])


if __name__ == '__main__':
    unittest.main()
