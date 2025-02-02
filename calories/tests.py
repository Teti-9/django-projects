from django.test import TestCase, Client

# Create your tests here.

class Testes(TestCase):
    def setUp(self):
        self.client = Client()

    def test_calorias(self):
        response = self.client.post('/api/calorias',
                                    {"carboidrato": 100,
                                     "proteina": 100,
                                     "gordura": 100},
                                     content_type="application/json")
        self.assertEqual(response.status_code, 200)