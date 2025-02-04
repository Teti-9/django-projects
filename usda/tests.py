from django.test import TestCase, Client

# Create your tests here.

class Testes(TestCase):
    def setUp(self):
        self.client = Client()

    def test_lista_alimentos(self):
        response = self.client.get(f'/api/alimento/carne moida')
        print(response.json())
        self.assertEqual(response.status_code, 200)