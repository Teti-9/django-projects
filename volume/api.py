from ninja import Router
from ninja.responses import JsonResponse
from .utils import calcular_series, calcular_residual
from muscleinfo.models import Exercicio
from users.utils import usuario
from src.utils import database_auth
# MONGODB
from mongodb.database import db
from muscleinfo.utils import individual_serial, list_serial

router = Router()
mongodb_auth = usuario
auth = database_auth()

@router.get('/exercicio/volumes', auth=auth)
def exercicio_volume_total(request):
    # SQL
    exercicio = Exercicio.objects.filter(user_id = usuario(request)).all()

    # MONGODB
    # exercicio = list_serial(db['muscleinfo_exercicio'].find({"user_id": usuario(request)}))

    if not exercicio:
        return JsonResponse({"Message": "Músculo não encontrado"}, status=404)

    series = calcular_series(exercicio)
    residual = calcular_residual(exercicio)

    response = {
            "Volume Primário": f"O volume primário total é de: {series}",
            "Volume Residual": f"O volume residual total é de: {residual}"
        }

    return response

@router.get('/exercicio/volume/{musculo}', auth=auth)
def exercicio_volume_unico(request, musculo: str):
    try:
        # SQL
        exercicio = Exercicio.objects.filter(musculo=musculo.title(), user_id = usuario(request)).all()

        # MONGODB
        # exercicio = list_serial(db['muscleinfo_exercicio'].find({"musculo": musculo.title(), "user_id": usuario(request)}))

        if not exercicio:
            return JsonResponse({"Message": "Músculo não encontrado"}, status=404)

        series = calcular_series(exercicio)
        residual = calcular_residual(exercicio)

        response = {
            "Volume Primário": f"O volume primário total para o músculo é de: {series}",
            "Volume Residual": f"O volume residual total para este músculo é de: {residual}"
        }

        return response
    except Exercicio.DoesNotExist:
        return JsonResponse({"detail": "Músculo não encontrado"}, status=404)