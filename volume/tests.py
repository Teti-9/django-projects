from django.test import TestCase, Client
from users.models import CustomUserModel as User
from muscleinfo.models import Exercicio

# Create your tests here.

class Testes(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='teste', email='teste', password='teste')
        self.client.login(username='teste', password='teste')

        self.exercicio = Exercicio.objects.create(
            nome="Teste", musculo="Teste", musculo_residual="Teste",
            series=1, infos="Teste", user_id=self.user.id
        )

    def test_exercicio_all_volume(self):
        response = self.client.get(f'/api/exercicio/volumes')
        self.assertEqual(response.status_code, 200)

    def test_exercicio_single_volume(self):
        response = self.client.get(f'/api/exercicio/volume/{self.exercicio.musculo}')
        self.assertEqual(response.status_code, 200)