from ninja import Router
from ninja.security import django_auth
from ninja.responses import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import CustomUserModel as User
from .schemas import CustomUserSchema

router = Router()

@router.post('/registrar')
def registrar(request, usuario: CustomUserSchema):
    try:
        usuario_logado = request.user.id

        if usuario_logado:
            return JsonResponse({"Message": "Não é possível se registrar estando logado em outra conta."}, status=404)
        
        User.objects.create_user(username=usuario.email, email=usuario.email, password=usuario.password)
        return {"Sucesso": "Usuário cadastrado com sucesso!"}
    
    except Exception as e:
        return {"Erro": (str(e))}
    
@router.post('/logar')
def logar(request, usuario: CustomUserSchema):

    usuario_logado = request.user.id

    if usuario_logado:
        return JsonResponse({"Message": "Deslogue para logar em outra conta."}, status=404)

    user = authenticate(request, email=usuario.email, password=usuario.password)

    if user is not None:
        login(request, user)
        return {"Message": "Logado com Sucesso!"}
    
    return {"Message": "Credenciais inválidas."}

@router.post('/deslogar', auth=django_auth)
def deslogar(request):

    logout(request)

    return {"Message": "Deslogado com sucesso!"}