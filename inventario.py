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

def validar_equipo_para_prestamo(inventario, codigo):
    ok, res = validar_no_vacio(codigo, "código")
    if not ok:
        return False, res
    codigo = res.upper()
    if codigo not in inventario:
        return False, f"El código {codigo} no existe."
    if inventario[codigo]["estado"] != DISPONIBLE:
        return False, f"El equipo {codigo} no está disponible."
    return True, codigo


def prestar_equipo(inventario, prestamos, codigo, estudiante, fecha):
    ok, res = validar_equipo_para_prestamo(inventario, codigo)
    if not ok:
        return False, res
    codigo = res
    ok, res = validar_no_vacio(estudiante, "estudiante")
    if not ok:
        return False, res
    estudiante = res
    inventario[codigo]["estado"] = PRESTADO
    prestamos.append({"codigo": codigo, "estudiante": estudiante, "fecha": fecha})
    return True, f"Préstamo de {codigo} a {estudiante} registrado."