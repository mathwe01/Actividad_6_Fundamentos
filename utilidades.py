def limpiar_texto(texto):
    return texto.strip()


def validar_no_vacio(valor, nombre_campo):
    valor = limpiar_texto(valor)
    if valor == "":
        return False, f"El campo '{nombre_campo}' no puede estar vacío."
    return True, valor

def validar_fecha(fecha):
    ok, resultado = validar_no_vacio(fecha, "fecha")
    if not ok:
        return False, resultado
    partes = resultado.split("/")
    if len(partes) != 3 or not all(p.isdigit() for p in partes):
        return False, "Formato de fecha inválido. Use dd/mm/yyyy."
    dia, mes, anio = (int(p) for p in partes)
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 2000):
        return False, "Fecha fuera de rango."
    return True, resultado