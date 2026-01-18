import unittest
import json
from app import app

class DashboardTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Progress Dashboard', response.data)

    def test_api_data_route(self):
        response = self.app.get('/api/dashboard-data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check structure
        self.assertIn('user', data)
        self.assertIn('metrics', data)
        self.assertIn('skills', data)
        self.assertIn('reminders', data)
        self.assertIn('recent_activity', data)
        
        # Check content
        self.assertEqual(data['user']['name'], 'Alex Johnson')
        self.assertEqual(data['metrics']['readiness']['score'], 82)

if __name__ == '__main__':
    unittest.main()
