## Django-Ninja + PostgreSQL / MongoDB

Esse projeto é uma junção de outros projetos meus que fornece uma API RESTful dentro da framework escolhida (Django-Ninja) para um back-end rápido e eficiente.

## Funcionalidades da API  

- 📌 **Exercícios:** CRUD (Criar, Ler, Atualizar, Deletar) de exercícios por nome ou músculo.  

- 📊 **Cálculo de Volume de Treino:** Volume semanal total ou filtrado por músculo.  

- 🔥 **Cálculo Calórico:** Retorna calorias totais com base em macronutrientes enviados via POST.  

- 🍖 **USDA API:** Query que retorna alimentos por meio de uma requisição HTTP.

- 🔐 **Autenticação:** Registro, login e logout de usuários.
## 🛠️ Instalação e Configuração

### 🔹 Instalação Local (SQLite)
```
git clone https://github.com/Teti-9/django_ninja-postgres.git
cd django_ninja-postgres
pip install -r requirements.txt

Altere a configuração de database para SQLite na pasta src > settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase.db',
        }
    }

Rode a aplicação na pasta raíz do projeto:
python manage.py runserver
```
### 🐳 Instalação com Docker + PostgreSQL
```
git clone https://github.com/Teti-9/django_ninja-postgres.git
cd django_ninja-postgres

Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:

POSTGRESQL_VERSION = 15
POSTGRESQL_USER = "usuario"
POSTGRESQL_PASS = "senha"
DATABASE = "sql" <- Deixe "sql" para utilizar SQLAlchemy/Django ORM.

Rode o comando:
docker compose up -d
```
### 🍃 Configuração MongoDB
```
Não é necessário editar o arquivo settings.py.

Crie uma database MongoDB com as seguintes collections:
muscleinfo_exercicio
users

Crie caso ainda não tenha um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:

MONGODB_URL = "mongodb+srv://usuario:senha@nomedatabase.ourq7.mongodb.net/"
DATABASE = "mongodb"

Dentro da pasta mongodb > database.py, altere o nome do banco de dados:
db = client.nomedatabase

O código para rodar os comandos MongoDB estão comentados dentro de cada endpoint.
Apenas comente os comandos SQL e descomente os comandos MongoDB.

Rode o comando para executar o servidor de acordo com a instalação escolhida acima.
```
## 🗂️ Estrutura do Back-end
- Cada funcionalidade está organizada em um app separado.  
- O arquivo `api.py` dentro de cada app contém os endpoints disponíveis.  

## 📄 Documentação
```
Siga os passos para instalação e inicie o servidor para ter acesso a documentação.

Local :
http://127.0.0.1:8000/api/docs

Docker :
http://localhost:8000/api/docs
```
