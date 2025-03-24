from ninja import Router
from argon2 import PasswordHasher
from ninja.responses import JsonResponse
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import CustomUserModel as User
from .schemas import CustomUserSchema
from src.utils import database_auth
from users.utils import usuario
# MONGODB Imports
from mongodb.database import db
import bson
from bson import ObjectId

router = Router()
ph = PasswordHasher()
auth = database_auth()

@router.post('/registrar')
def registrar(request, usuario_: CustomUserSchema):
    # SQL
    if usuario(request):
        return JsonResponse({"Message": "Não é possível se registrar estando logado em outra conta."}, status=404)

    try:
        User.objects.create_user(username=usuario_.email, email=usuario_.email, password=usuario_.password)
    except IntegrityError:
        return JsonResponse({"Message": "Email já cadastrado!"}, status=409)

    # MONGODB
    # usuario_existe = db['users'].find_one({"email": usuario_.email})
    
    # if usuario_existe:
    #     return JsonResponse({"Message": "Email já cadastrado!"}, status=409)
    
    # if usuario(request):
    #     return JsonResponse({"Message": "Não é possível se registrar estando logado em outra conta."}, status=404)
    
    # user = {
    #     "email": usuario_.email,
    #     "password": ph.hash(usuario_.password)
    # }
    # user = db['users'].insert_one(user)

    return JsonResponse({"Message": "Usuário cadastrado com sucesso!"}, status=200)
    
@router.post('/logar')
def logar(request, usuario_: CustomUserSchema):
    # SQL
    if usuario(request):
        return JsonResponse({"Message": "Usuário já está autenticado!"}, status=404)

    user = authenticate(request, email=usuario_.email, password=usuario_.password)

    if user is not None:
        login(request, user)
        return JsonResponse({"Message": "Logado com sucesso!"}, status=200)

    # MONGODB
    # if usuario(request):
    #     return JsonResponse({"Message": "Usuário já está autenticado!"}, status=404)
    
    # user = db['users'].find_one({"email": usuario_.email})
    # if user and ph.verify(user['password'], usuario_.password):
    #     request.session['user_id'] = str(user['_id'])
    #     return JsonResponse({"Message": "Logado com sucesso!"}, status=200)

    return JsonResponse({"Message": "Credenciais inválidas!"}, status=404)

@router.post('/deslogar', auth=auth)
def deslogar(request):
    # SQL
    logout(request)

    # MONGODB
    # request.session.flush()

    return JsonResponse({"Message": "Deslogado com sucesso!"}, status=200)