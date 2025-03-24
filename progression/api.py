from ninja import Router
from ninja.responses import JsonResponse
from src.utils import database_auth
from users.utils import usuario
from .utils import check_progression
from muscleinfo.models import Exercicio
# MONGODB
from mongodb.database import db
from muscleinfo.utils import individual_serial, regex_pattern

router = Router()
auth = database_auth()

@router.get('/exercicio/progressao/{nome}', auth=auth)
def progressao(request, nome: str):
    # SQL
    exercicio = Exercicio.procurar.filter(nome__icontains=nome.title(), user_id = usuario(request)).first()

    if not exercicio:
        return JsonResponse({"Message": "Exercício não encontrado"}, status=404)

    # MONGODB
    # try:
    #     exercicio = individual_serial(db['muscleinfo_exercicio'].find_one({"nome": {"$regex": regex_pattern(nome)}, "user_id": usuario(request)}))
    # except TypeError:
    #     return JsonResponse({"Message": "Exercício não encontrado"}, status=404)
    
    data = None
    data_anterior = None

    data = exercicio.get("data") if isinstance(exercicio, dict) else getattr(exercicio, "data", None)
    data_anterior = exercicio.get("data_anterior") if isinstance(exercicio, dict) else getattr(exercicio, "data_anterior", None)

    try:
        data = data.strftime('%d/%m/%Y')
        data_anterior = exercicio.get("data_anterior") if isinstance(exercicio, dict) else getattr(exercicio, "data_anterior", None)
        data_anterior = data_anterior.strftime('%d/%m/%Y')
    except:
        pass
    
    prog = check_progression(exercicio)

    resultado = {
        1: "Você progrediu tanto carga quanto repetições.",
        2: "Você progrediu se mantendo nas mesmas repetições para uma carga maior.",
        3: "Você ainda está progredindo repetições para essa carga, devendo chegar ao mesmo número de repetições que atingiu anteriormente para ser considerado uma progressão.",
        4: "Você se manteve na mesma carga para as mesmas repetições, mas talvez tenha progredido em técnica ou execução.",
        5: "Não há dados suficientes para determinar se houve progressão ou não.",
        6: "Você progrediu aumentando as repetições para a mesma carga.",
        7: "Você regrediu em repetições comparado a última atualização para a mesma carga.",
        8: "Você não progrediu no quesito carga ou repetições, mas talvez tenha progredido em técnica ou execução."
    }

    message = resultado.get(prog)

    response = {
        "Nome": exercicio.get("nome") if isinstance(exercicio, dict) else getattr(exercicio, "nome", None),
        "Musculo": exercicio.get("musculo") if isinstance(exercicio, dict) else getattr(exercicio, "musculo", None),
        "Carga": exercicio.get("carga") if isinstance(exercicio, dict) else getattr(exercicio, "carga", None),
        "Carga Anterior": exercicio.get("carga_anterior") if isinstance(exercicio, dict) else getattr(exercicio, "carga_anterior", None),
        "Repetições": exercicio.get("repeticoes") if isinstance(exercicio, dict) else getattr(exercicio, "repeticoes", None),
        "Repetições Anterior": exercicio.get("repeticoes_anterior") if isinstance(exercicio, dict) else getattr(exercicio, "repeticoes_anterior", None),
        "Data": data,
        "Data Anterior": data_anterior,
        "Conclusão": message
    }

    return JsonResponse(response, status=200)