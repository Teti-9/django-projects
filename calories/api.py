from ninja import Router
from ninja.responses import JsonResponse
from .schemas import CaloriaSchema

router = Router()

CARB = 4
PROTEINA = 4
GORDURA = 9

@router.post('/calorias')
def calorias(request, caloria: CaloriaSchema):

    for i in caloria:
        if i[1] < 0:
            macro = i[0]
            return JsonResponse({"Erro": f"Macronutriente *{macro.title()}* não pode ser negativo."}, status=400)

    carboidrato = caloria.carboidrato * CARB
    proteina = caloria.proteina * PROTEINA
    gordura = caloria.gordura * GORDURA

    calculo = carboidrato + proteina + gordura

    return JsonResponse({"Calorias": calculo}, status=200)