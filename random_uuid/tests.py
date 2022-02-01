from django.test import TestCase
from rest_framework.test import APIClient
from unittest import mock


class TestRandomUUID(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/generate_uuid/"

    def test_random_uuid(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    @mock.patch("random_uuid.views.uuid.uuid4")
    def test_random_uuid_mock_value(self, uuid_mocker):
        result = uuid_mocker.return_value = "12345678-1234-1234-1234-123456789012"
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

        key = list(response.json().keys())[0]
        self.assertEqual(response.json()[key], result)
