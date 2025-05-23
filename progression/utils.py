def check_progression(exercise):
    def get_attr(obj, attr):
        return obj.get(attr) if isinstance(obj, dict) else getattr(obj, attr, None)

    repeticoes = get_attr(exercise, "repeticoes")
    repeticoes_anterior = get_attr(exercise, "repeticoes_anterior")
    carga = get_attr(exercise, "carga")
    carga_anterior = get_attr(exercise, "carga_anterior")

    if any(val is None for val in [repeticoes, repeticoes_anterior, carga, carga_anterior]):
        return 5
    
    if repeticoes_anterior == 0 or carga_anterior == 0:
        return 5

    if carga > carga_anterior:
        if repeticoes > repeticoes_anterior:
            return 1
        elif repeticoes == repeticoes_anterior:
            return 2
        else:
            return 3
        
    elif carga == carga_anterior:
        if repeticoes > repeticoes_anterior:
            return 6
        elif repeticoes == repeticoes_anterior:
            return 4
        else:
            return 7
        
    else:
        return 8