def check_progression(exercicio):
    repeticoes = exercicio.get("repeticoes") if isinstance(exercicio, dict) else getattr(exercicio, "repeticoes", None)
    repeticoes_anterior = exercicio.get("repeticoes_anterior") if isinstance(exercicio, dict) else getattr(exercicio, "repeticoes_anterior", None)
    carga = exercicio.get("carga") if isinstance(exercicio, dict) else getattr(exercicio, "carga", None)
    carga_anterior = exercicio.get("carga_anterior") if isinstance(exercicio, dict) else getattr(exercicio, "carga_anterior", None)

    if None in (repeticoes, repeticoes_anterior, carga, carga_anterior):
        return 5

    if repeticoes_anterior == 0 or carga_anterior == 0:
        return 5
    elif repeticoes_anterior is None or carga_anterior is None:
        return 5
    elif repeticoes > repeticoes_anterior and carga > carga_anterior:
        return 1
    elif repeticoes == repeticoes_anterior and carga > carga_anterior:
        return 2
    elif repeticoes < repeticoes_anterior and carga > carga_anterior:
        return 3
    elif repeticoes == repeticoes_anterior and carga == carga_anterior:
        return 4
    elif repeticoes > repeticoes_anterior and carga == carga_anterior:
        return 6
    elif repeticoes < repeticoes_anterior and carga == carga_anterior:
        return 7
    else:
        return 8
    
# exercicio criado recentemente = 5
# repetições aumentaram e carga aumentou = 1
# repetições iguais e carga aumentou = 2
# repetições diminuiram e carga aumentou = 3
# repetições iguais e carga iguais = 4
# repetições maiores para mesma carga = 6
# repetições diminuiram e carga diminiu = False