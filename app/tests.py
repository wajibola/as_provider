from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class ASInfoTests(TestCase):
    def setUp(self):
        self.client = Client()
    def test_get_as_info(self):
        response = self.client.get(reverse('as_info', args=[9700]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 3)

    def test_as_info_not_found(self):
        response = self.client.get(reverse('as_info', args=[999999]))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['data'], {})

    def test_get_as_info_by_ip(self):
        response = self.client.get(reverse('ip_as_info', args=['172.68.25.0']))
        self.assertEqual(response.status_code, 200)

    def test_get_as_info_invalid_ip(self):
        response = self.client.get(reverse('ip_as_info', args=['invalid_ip']))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Invalid IP address')

    def test_as_info_by_ip_not_found(self):
        response = self.client.get(reverse('ip_as_info', args=['999999']))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['data'], {})
