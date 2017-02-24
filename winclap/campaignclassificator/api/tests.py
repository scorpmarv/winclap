import os
import json
from django.test import TestCase
from django.urls import reverse


class TestCalls(TestCase):
    def setUp(self):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, '..', 'datasets', 'user.json')
        with open(file_path) as f:
            self.user_data = json.load(f)

    def test_with_json_file_find(self):
        response = self.client.get(reverse('best_campaign'), self.user_data)
        self.assertIn(
            response.data,
            [{
                "id": 1,
                "name": "Uber",
                "gender": "All",
                "min_age": 16,
                "max_age": 45,
                "platform": "Android",
                "connection": "All"
            },
            {
                "name": "Pokemon Go",
                "max_age": 18,
                "connection": "Mobile data",
                "gender": "Male",
                "min_age": 15,
                "id": 2,
                "platform": "Android"
            }]
        )

    def test_with_json_file_empty(self):
        response = self.client.get(reverse('best_campaign'), self.user_data)
        self.assertNotIn(
            response.data,
            [{
                "id": 3,
                "name": "Spotify",
                "gender": "All",
                "min_age": None,
                "max_age": None,
                "platform": "iOS",
                "connection": "All"
            },
            {
                "id":4,
                "name": "Sweet Selfie",
                "gender": "Female",
                "min_age": 12,
                "max_age": 30,
                "platform": "Android",
                "connection": "WiFi"
            },
            {
                "id": 5,
                "name": "Sweet Selfie",
                "gender": "Female",
                "min_age": 12,
                "max_age": 30,
                "platform": "iOS",
                "connection": "WiFi"
            },
            {
                "id": 6,
                "name": "OLX",
                "gender": "All",
                "min_age": 18,
                "max_age": None,
                "platform": "iOS",
                "connection": "All"
            }]
        )

    def test_with_json_missing_argument(self):
        del self.user_data['platform']
        response = self.client.get(reverse('best_campaign'), self.user_data)
        self.assertEqual(response.status_code, 400)

    def test_with_json_bad_argument(self):
        self.user_data['connection'] = 'blank'
        response = self.client.get(reverse('best_campaign'), self.user_data)
        self.assertEqual(response.status_code, 400)