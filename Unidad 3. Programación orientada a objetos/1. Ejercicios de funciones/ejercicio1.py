def comprobarDNI(dni : str) -> bool:
    """Comprueba si un DNI es válido

    Args:
        dni (str): El DNI que queremos comprobar

    Returns:
        (bool): Si el DNI es válido o no
    """

    valido = True

    if len(dni) != 9:
        valido = False

    numero = dni[:8]
    letra = dni[8].upper()

    if not numero.isdigit():
        valido = False

    numero = int(numero)

    resto = numero % 23

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    if letras[resto] != letra:
        valido = False

    return valido

print(comprobarDNI("12345678z"))