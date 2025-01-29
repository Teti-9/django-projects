from ninja import Router
from ninja.security import django_auth
from ninja.responses import JsonResponse
from django.middleware.csrf import get_token
from .models import Exercicio
from .schemas import ExercicioSchema, ExercicioSchemaNoID, ExercicioSchemaEdit
from typing import List
from users.utils import usuario

router = Router()

@router.get('/csrf-token')
def get_csrf_token(request):
    return get_token(request)

@router.post('/populardb', response = ExercicioSchema, auth=django_auth)
def populardb(request, exercicio: ExercicioSchemaNoID):
    exerc = exercicio.dict()

    for key, value in exerc.items():
        if isinstance(value, str):
            exerc[key] = value.title()

    exerc['user_id'] = usuario(request)
    
    exercicio = Exercicio(**exerc)
    exercicio.save()
    return exercicio

@router.get('/exercicio/nome/{nome}', response = List[ExercicioSchema], auth=django_auth)
def procurar_exercicio_nome(request, nome: str):
    try:

        exercicio = Exercicio.objects.filter(nome__icontains=nome.title(), user_id = usuario(request))
        
        if len(exercicio) <= 0:
            return JsonResponse({"detail": "Exercício não encontrado"}, status=404)

        return exercicio
    except Exercicio.DoesNotExist:
        return JsonResponse({"detail": "Exercício não encontrado"}, status=404)

@router.get('/exercicio/musculo/{musculo}', response=List[ExercicioSchema], auth=django_auth)
def procurar_exercicio_musculo(request, musculo: str):
    try:
        exercicios = Exercicio.objects.filter(musculo=musculo.title(), user_id = usuario(request)).all()

        if len(exercicios) <= 0:
            return JsonResponse({"detail": "Músculo não encontrado"}, status=404)

        return exercicios
    except Exercicio.DoesNotExist:
        return JsonResponse({"detail": "Exercício não encontrado"}, status=404)

@router.put('/exercicio/editar/{id}', response = ExercicioSchemaEdit, auth=django_auth)
def editar_exercicio(request, id: int, exercicio: ExercicioSchemaEdit):
    try:
        exercicio_obj = Exercicio.objects.get(id=id, user_id = usuario(request))

        for key, value in exercicio.dict().items():
            if value is None:
                pass
            else:
                if isinstance(value, str):
                    setattr(exercicio_obj, key, value.title())
                else:
                    setattr(exercicio_obj, key, value)

        exercicio_obj.save()
        return JsonResponse({"detail": "Exercício atualizado com sucesso!"}, status=200)
    except Exercicio.DoesNotExist:
        return JsonResponse({"detail": "Exercício não encontrado"}, status=404)

@router.delete('/exercicio/deletar/{id}', auth=django_auth)
def deletar_exercicio(request, id: int):
    try:
        exercicio = Exercicio.objects.get(id=id, user_id = usuario(request))
        exercicio.delete()
        return JsonResponse({"detail": "Exercício deletado com sucesso!"}, status=200)
    except Exercicio.DoesNotExist:
        return JsonResponse({"detail": "Exercício não encontrado"}, status=404)