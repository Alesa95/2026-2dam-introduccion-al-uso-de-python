def convertirTemperatura(temperatura_inicial : float, unidad_inicial : str, unidad_final : str) -> float:
    """Convierte la temperatura de una unidad a otra

    Params:
        temperatura_inicial (float): La temperatura que queremos convertir a otra unidad
        unidad_inicial (str): La unidad en la que se encuentra la temperatura inicial
        unidad_final (str): La unidad a la que queremos convertir la temperatura

    Returns:
        (float): La temperatura inicial convertida de la unidad inicial a la unidad final
    """
    if unidad_inicial not in ["C", "F", "K"] or unidad_final not in ["C", "F", "K"]:
        raise ValueError("Las unidades posibles solo pueden ser C, F o K")

    temperatura_final = temperatura_inicial
    unidad_inicial = unidad_inicial.upper()
    unidad_final = unidad_final.upper()

    if unidad_inicial == "C":
        if temperatura_inicial < -273.15:
            raise ValueError("La temperatura inicial no puede ser inferior a -273.15 C")
        if unidad_final == "F":
            temperatura_final = (temperatura_inicial * (9/5)) + 32
        elif unidad_final == "K":
            temperatura_final = temperatura_inicial + 273.15
    elif unidad_inicial == "F":
        if temperatura_inicial < -459.67:
            raise ValueError("La temperatura inicial no puede ser inferior a -459.67 F")
        if unidad_final == "C":
            temperatura_final = (temperatura_inicial - 32) * (5/9)
        elif unidad_final == "K":
            temperatura_final = ((temperatura_inicial - 32) * (5/9)) + 273.15
    elif unidad_inicial == "K":
        if temperatura_inicial < 0:
            raise ValueError("La temperatura inicial no puede ser inferior a 0 K")
        if unidad_final == "C":
            temperatura_final = temperatura_inicial - 273.15
        elif unidad_final == "F":
            temperatura_final = ((temperatura_inicial - 273.15) * (9/5)) + 32

    return round(temperatura_final,2)

print(convertirTemperatura(10,"C","F"))