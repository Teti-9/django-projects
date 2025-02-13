def calcular_series(parametro):
    series = {}

    exercicios = parametro

    for exercicio in exercicios:
        musculo = exercicio.get("musculo") if isinstance(exercicio, dict) else getattr(exercicio, "musculo", None)
        if musculo:
            series[musculo] = series.get(musculo, 0) + (
                exercicio.get("series") if isinstance(exercicio, dict) else getattr(exercicio, "series", 0))

    for musculo, count in series.items():
        series[musculo] = f"{count} séries semanais"

    if not series:
        series = "Não há volume primário."

    return series

def calcular_residual(parametro):
    residual = {}

    exercicios = parametro

    for exercicio in exercicios:
        musculo_residual = exercicio.get("musculo_residual") if isinstance(exercicio, dict) else getattr(exercicio,
                                                                                                         "musculo_residual",
                                                                                                         None)
        if musculo_residual:
            series_value = exercicio.get("series", 0) if isinstance(exercicio, dict) else getattr(exercicio, "series",
                                                                                                  0)
            residual[musculo_residual] = residual.get(musculo_residual, 0) + series_value * 0.5

    for musculo, count in residual.items():
        residual[musculo] = f"{count:.1f} séries semanais"

    if not residual:
        residual = "Não há volume residual."

    return residual