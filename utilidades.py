def limpiar_texto(texto):
    return texto.strip()


def validar_no_vacio(valor, nombre_campo):
    valor = limpiar_texto(valor)
    if valor == "":
        return False, f"El campo '{nombre_campo}' no puede estar vacío."
    return True, valor