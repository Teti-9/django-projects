## Django-Ninja + PostgreSQL

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

- Rode a aplicação na pasta raíz do projeto:
python manage.py runserver
```
### 🐳 Instalação com Docker + PostgreSQL
```
git clone https://github.com/Teti-9/django_ninja-postgres.git
cd django_ninja-postgres

- Edite/crie o arquivo .env caso queira, ou edite o arquivo docker-compose.yml diretamente:

POSTGRESQL_VERSION=15
POSTGRESQL_PASS=senha

- Atualmente o docker está rodando sem porta fixa, edite o arquivo caso necessário.

ports:
    - "8000" > "8000:8000"

- Rode o comando:
docker compose up -d

```

## 🗂️ Estrutura do Back-end
- Cada funcionalidade está organizada em um app separado.  
- O arquivo `api.py` dentro de cada app contém os endpoints disponíveis.  

## Documentação
```
Siga os passos para instalação e inicie o servidor para ter acesso a documentação.

http://127.0.0.1:8000/api/docs
http://localhost:{Porta-Docker}/api/docs
```