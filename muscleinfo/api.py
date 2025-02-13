from ninja import Router
from ninja.responses import JsonResponse
from django.middleware.csrf import get_token
from .models import Exercicio
from .schemas import ExercicioSchema, ExercicioSchemaNoID, ExercicioSchemaEdit
from typing import List, Union
from users.utils import usuario
from src.utils import database_auth
# MONGODB Imports
from mongodb.database import db
from .utils import individual_serial, list_serial, regex_pattern
import bson
from bson import ObjectId

router = Router()
auth = database_auth()

@router.get('/csrf-token')
def get_csrf_token(request):
    return get_token(request)

@router.post('/populardb', response = ExercicioSchema, auth=auth)
def populardb(request, exercicio: ExercicioSchemaNoID):

    update_data = {}
    for key, value in exercicio.dict().items():
        if value is not None:
            update_data[key] = value.title() if isinstance(value, str) else value

    update_data['user_id'] = usuario(request)

    # SQL
    exercicio = Exercicio(**update_data)
    exercicio.save()
    return exercicio

    # MONGODB
    # exercicio = db['muscleinfo_exercicio'].insert_one(update_data)
    # update_data['id'] = str(exercicio.inserted_id)
    # return update_data

@router.get('/exercicio/nome/{nome}', response = List[ExercicioSchema], auth=auth)
def procurar_exercicio_nome(request, nome: str):
    try:

        # SQL
        exercicio = Exercicio.objects.filter(nome__icontains=nome.title(), user_id = usuario(request))

        # MONGODB
        # exercicio = list_serial(db['muscleinfo_exercicio'].find({"nome": {"$regex": regex_pattern(nome)},
        #                                                          "user_id": usuario(request)}))

        if not exercicio:
            return JsonResponse({"Message": "Exercício não encontrado"}, status=404)

        return exercicio

    except Exercicio.DoesNotExist:
        return JsonResponse({"Message": "Exercício não encontrado"}, status=404)
    except Exception as e:
        return JsonResponse({"Message": f"Erro: {str(e)}"}, status=500)

@router.get('/exercicio/musculo/{musculo}', response=List[ExercicioSchema], auth=auth)
def procurar_exercicio_musculo(request, musculo: str):
    try:
        # SQL
        exercicios = Exercicio.objects.filter(musculo=musculo.title(), user_id = usuario(request)).all()

        # MONGODB
        # exercicios = list_serial(db['muscleinfo_exercicio'].find({"musculo": {"$regex": regex_pattern(musculo)},
        #                                                           "user_id": usuario(request)}))

        if not exercicios:
            return JsonResponse({"Message": "Músculo não encontrado"}, status=404)

        return exercicios

    except Exercicio.DoesNotExist:
        return JsonResponse({"Message": "Exercício não encontrado"}, status=404)
    except Exception as e:
        return JsonResponse({"Message": f"Erro: {str(e)}"}, status=500)

@router.put('/exercicio/editar/{id}', response = ExercicioSchemaEdit, auth=auth)
def editar_exercicio(request, id: Union[int, str], exercicio: ExercicioSchemaEdit):
    try:

        # SQL
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

        # MONGODB
        # update_data = {}
        # for key, value in exercicio.dict().items():
        #     if value is not None:
        #         update_data[key] = value.title() if isinstance(value, str) else value
        #
        # id = ObjectId(id)
        # editar = db['muscleinfo_exercicio'].find_one_and_update({"_id": id, "user_id": usuario(request)}, {"$set": update_data})
        #
        # if not editar:
        #     return JsonResponse({"Message": "Exercício não encontrado"}, status=404)

        return JsonResponse({"Message": "Exercício atualizado com sucesso!"}, status=200)

    except Exercicio.DoesNotExist:
        return JsonResponse({"Message": "Exercício não encontrado"}, status=404)
    except bson.errors.InvalidId:
        return JsonResponse({"Message": "ID Inválido!"}, status=404)
    except Exception as e:
        return JsonResponse({"Message": f"Erro: {str(e)}"}, status=500)

@router.delete('/exercicio/deletar/{id}', auth=auth)
def deletar_exercicio(request, id: Union[int, str]):
    try:

        # SQL
        exercicio = Exercicio.objects.get(id=id, user_id = usuario(request))
        exercicio.delete()

        # MONGODB
        # id = ObjectId(id)
        # deletar = db['muscleinfo_exercicio'].find_one_and_delete({"_id": id, "user_id": usuario(request)})
        #
        # if not deletar:
        #     return JsonResponse({"Message": "Exercício não encontrado"}, status=404)

        return JsonResponse({"Message": "Exercício deletado com sucesso!"}, status=200)

    except Exercicio.DoesNotExist:
        return JsonResponse({"Message": "Exercício não encontrado"}, status=404)
    except bson.errors.InvalidId:
        return JsonResponse({"Message": "ID Inválido!"}, status=404)
    except Exception as e:
        return JsonResponse({"Message": f"Erro: {str(e)}"}, status=500)