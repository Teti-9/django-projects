def calcular_series(parametro):
    series = {}

    exercicios = parametro

    for exercicio in exercicios:
        musculo = exercicio.musculo
        if musculo: 
            series[musculo] = series.get(musculo, 0) + exercicio.series

    for musculo, count in series.items():
        series[musculo] = f"{count} séries semanais"

    if not series:
        series = "Não há volume primário."

    return series

def calcular_residual(parametro):
    residual = {}

    exercicios = parametro

    for exercicio in exercicios:
        musculo_residual = exercicio.musculo_residual
        if musculo_residual:
            residual[musculo_residual] = residual.get(musculo_residual, 0) + exercicio.series * 0.5

    for musculo, count in residual.items():
        residual[musculo] = f"{count:.1f} séries semanais"

    if not residual:
        residual = "Não há volume residual."

    return residual