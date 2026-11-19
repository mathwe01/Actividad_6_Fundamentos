from utilidades import validar_no_vacio

DISPONIBLE = "disponible"
PRESTADO = "prestado"


def crear_inventario():
    return {}


def registrar_equipo(inventario, codigo, nombre, categoria):
    for valor, campo in ((codigo, "código"), (nombre, "nombre"), (categoria, "categoría")):
        ok, res = validar_no_vacio(valor, campo)
        if not ok:
            return False, res
    codigo = codigo.strip().upper()
    if codigo in inventario:
        return False, f"El código {codigo} ya está registrado."
    inventario[codigo] = {"nombre": nombre.strip(),
                          "categoria": categoria.strip().lower(),
                          "estado": DISPONIBLE}
    return True, f"Equipo {codigo} registrado correctamente."