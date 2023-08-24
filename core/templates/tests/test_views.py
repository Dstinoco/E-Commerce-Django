from django.test import TestCase


class IndexViesTestCase(TestCase):
    def test_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)