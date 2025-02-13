from dotenv import load_dotenv
from users.utils import usuario
from ninja.security import django_auth
import os

load_dotenv()

def database_auth():
    return usuario if os.environ.get('DATABASE') == 'mongodb' else django_auth