from django.test import TestCase, Client
from users.models import CustomUserModel as User

# Create your tests here.

class Testes(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='teste', email='teste', password='teste')

    def test_registrar(self):
        response = self.client.post('/api/registrar',
                                    {"username": "teste",
                                     "email": "teste",
                                     "password": "teste"},
                                     content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_logar(self):
        response = self.client.post('/api/logar',
                                    {"email": "teste",
                                     "password": "teste"},
                                     content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_deslogar(self):
        self.client.login(username='teste', password='teste')
        response = self.client.post('/api/deslogar')
        self.assertEqual(response.status_code, 200)