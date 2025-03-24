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
            series=0, carga=0, repeticoes=0, infos="Teste", user_id=self.user.id
        )

    def test_get_csrf_token(self):
        response = self.client.get('/api/csrf-token')
        self.assertEqual(response.status_code, 200)

    def test_populardb(self):
        response = self.client.post('/api/populardb',
                               {"nome": self.exercicio.nome,
                                "musculo": self.exercicio.musculo,
                                "musculo_residual": self.exercicio.musculo_residual,
                                "series": self.exercicio.series,
                                "carga": self.exercicio.carga,
                                "repeticoes": self.exercicio.repeticoes,
                                "infos": self.exercicio.infos},
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_procurar_exercicio_nome(self):
        response = self.client.get(f'/api/exercicio/nome/{self.exercicio.nome}')
        self.assertEqual(response.status_code, 200)

    def test_procurar_exercicio_musculo(self):
        response = self.client.get(f'/api/exercicio/musculo/{self.exercicio.musculo}')
        self.assertEqual(response.status_code, 200)

    def test_editar_exercicio(self):
        response = self.client.put(f'/api/exercicio/editar/{self.exercicio.id}',
                               {"nome": self.exercicio.nome,
                                "musculo": self.exercicio.musculo,
                                "musculo_residual": self.exercicio.musculo_residual,
                                "series": self.exercicio.series,
                                "infos": self.exercicio.infos},
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_delete_exercicio(self):
        response = self.client.delete(f'/api/exercicio/deletar/{self.exercicio.id}')
        self.assertEqual(response.status_code, 200)