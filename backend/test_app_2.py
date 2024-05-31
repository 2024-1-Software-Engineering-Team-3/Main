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

    #-------------------- REGISTER TESTCASE -----------------------------------------------#

    def test_register_user_failed_2(self):
        response = self.client.post('/Login/signup', json={
        })
        self.assertEqual(response.status_code, 400)

    def test_register_user_failed_1(self): #failed case when username is ommited
        response = self.client.post('/Login/signup', json={
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 400)

    def test_register_user(self): #normal flow testcase
        response = self.client.post('/Login/signup', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('회원가입이 성공적으로 완료되었습니다.', response.get_json()['Response'])

    #----------------------------------------------------------------------------------------#

    #-------------------- LOGIN TESTCASE -----------------------------------------------#

    def test_login_user_failed_2(self):
        self.test_register_user()
        response = self.client.post('/Login/login', json={
        })
        self.assertEqual(response.status_code, 401)
        
    def test_login_user_failed_1(self):
        self.test_register_user()
        response = self.client.post('/Login/login', json={
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 401)

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

    #----------------------------------------------------------------------------------------#


    #-------------------- RECRUITING TESTCASE -----------------------------------------------#

    def test_recruiting_create_failed_2(self):
        self.test_login_user()
        response = self.client.post('/Recruitment/upload', json={
        })
        self.assertEqual(response.status_code, 400)
    
    def test_recruiting_create_failed_1(self):
        self.test_login_user()
        response = self.client.post('/Recruitment/upload', json={
            'title': 'New Study Group',
            'description': 'A new study group for advanced topics.',
            'membercount': 10,
            'duration': '3 months',
            'type': 'study'
        })
        self.assertEqual(response.status_code, 201)


    def test_recruiting_create(self):
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

    def test_recruiting_join_failed_1(self):
        self.test_recruiting_create()
        response = self.client.post('/Recruitment/join', json={
            'user_id': -1,
            'recruitment_id': 1
        })
        self.assertEqual(response.status_code, 201)
    
    def test_recruiting_join(self):
        self.test_recruiting_create()
        response = self.client.post('/Recruitment/join', json={
            'user_id': 1,
            'recruitment_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("성공적으로 리크루먼트에 가입했습니다.", response.get_json()['Response'])

    #----------------------------------------------------------------------------------------#

    def test_qa_create_failed_1(self):
        self.test_login_user()
        response = self.client.post('/QA/upload', json={
            "title": "new title",
            "content": "This is a content",
            "user_id": 1,
            "answered": False
        })
        self.assertEqual(response.status_code, 201)
    
    def test_qa_create(self):
        self.test_login_user()
        response = self.client.post('/QA/upload', json={
            "title": "new title",
            "content": "This is a content",
            "user_id": 1,
            "point": 10,
            "answered": False
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['Response'], 'QA entry가 성공적으로 생성되었습니다.')

        with self.app.app_context():
            qa_entry = QAEntry.query.filter_by(id=data['id']).first()
            self.assertIsNotNone(qa_entry)
            self.assertEqual(qa_entry.title, 'new title')
            self.assertEqual(qa_entry.content, 'This is a content')
            self.assertEqual(qa_entry.user_id, 1)
            self.assertEqual(qa_entry.point, 10)
            self.assertFalse(qa_entry.answered)
    
    def test_qa_get(self):
        self.test_qa_create()
        response = self.client.get('/QA/home')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['Response'], 'Success')
        self.assertEqual(len(data['Questions']), 1)
        self.assertEqual(data['Questions'][0]['title'], 'new title')
        self.assertEqual(data['Questions'][0]['content'], 'This is a content')
        self.assertEqual(data['Questions'][0]['userid'], 1)
        self.assertEqual(data['Questions'][0]['username'], 'testuser')
        self.assertEqual(data['Questions'][0]['point'], 10)
        self.assertEqual(data['Questions'][0]['answered'], False)


if __name__ == '__main__':
    print("-"*70)
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2)
