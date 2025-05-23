from ninja import Router
from .utils import calcular_series, calcular_residual
from django.shortcuts import get_list_or_404
from muscleinfo.models import Exercicio
from users.utils import usuario
from src.utils import database_auth
# MONGODB
from mongodb.database import db
from muscleinfo.utils import list_serial

router = Router()
auth = database_auth()

@router.get('/exercicio/volumes', auth=auth)
def exercicio_volume_total(request):
    # SQL
    volume = get_list_or_404(
        Exercicio.procurar.filter(
            user_id = usuario(request)))

    # MONGODB
    # volume = list_serial(db['muscleinfo_exercicio'].find({"user_id": usuario(request)}))

    series = calcular_series(volume)
    residual = calcular_residual(volume)

    response = {
            "Volume Primário": f"O volume primário total é de: {series}",
            "Volume Residual": f"O volume residual total é de: {residual}"
        }

    return response

@router.get('/exercicio/volume/{musculo}', auth=auth)
def exercicio_volume_unico(request, musculo: str):
    # SQL
    volume = get_list_or_404(
        Exercicio.procurar.filter(
            musculo=musculo.title(), 
            user_id = usuario(request)))

    # MONGODB
    # volume = list_serial(db['muscleinfo_exercicio'].find({"musculo": musculo.title(), "user_id": usuario(request)}))

    series = calcular_series(volume)
    residual = calcular_residual(volume)

    response = {
        "Volume Primário": f"O volume primário total para o músculo é de: {series}",
        "Volume Residual": f"O volume residual total para este músculo é de: {residual}"
    }

    return response