from ninja import Router
from ninja.security import django_auth
from ninja.responses import JsonResponse
from .utils import calcular_series, calcular_residual
from muscleinfo.models import Exercicio
from users.utils import usuario

router = Router()

@router.get('/exercicio/volumes', auth=django_auth)
def exercicio_all_volume(request):
    exercicio = Exercicio.objects.filter(user_id = usuario(request)).all()

    series = calcular_series(exercicio)

    residual = calcular_residual(exercicio)

    response = {
            "Volume Primário": f"O volume primário total é de: {series}",
            "Volume Residual": f"O volume residual total é de: {residual}"
        }

    return response

@router.get('/exercicio/volumes/{musculo}', auth=django_auth)
def exercicio_single_volume(request, musculo: str):
    try:
        exercicio = Exercicio.objects.filter(musculo=musculo.title(), user_id = usuario(request)).all()

        series = calcular_series(exercicio)

        residual = calcular_residual(exercicio)

        response = {
            "Volume Primário": f"O volume primário total para o músculo é de: {series}",
            "Volume Residual": f"O volume residual total para este músculo é de: {residual}"
        }

        return response
    except Exercicio.DoesNotExist:
        return JsonResponse({"detail": "Músculo não encontrado"}, status=404)