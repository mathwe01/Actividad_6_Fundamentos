import inventario as inv

def nuevo():
    i, p = inv.crear_inventario(), []
    inv.registrar_equipo(i, "L01", "Laptop Lenovo", "laptop")
    inv.registrar_equipo(i, "L02", "Laptop HP", "laptop")
    inv.registrar_equipo(i, "M01", "Mouse Logitech", "mouse")
    return i, p

def probar(nombre, entrada, esperado, accion):
    ok, msg = accion()
    print(f"{'OK ' if ok == esperado else 'FALLO'} | {nombre} | {entrada} | {msg}")
    
i, p = nuevo()
probar("Préstamo válido", "L01, Ana Lopez, 19/11/2026", True,
       lambda: inv.prestar_equipo(i, p, "L01", "Ana Lopez", "19/11/2026"))
probar("Equipo no disponible", "L01 ya prestado", False,
       lambda: inv.prestar_equipo(i, p, "L01", "Luis", "19/11/2026"))
probar("Código inexistente", "X99", False,
       lambda: inv.prestar_equipo(i, p, "X99", "Luis", "19/11/2026"))
probar("Dato vacío", "estudiante vacío", False,
       lambda: inv.prestar_equipo(i, p, "L02", "  ", "19/11/2026"))
probar("Fecha inválida", "32/13/2026", False,
       lambda: inv.prestar_equipo(i, p, "L02", "Ana Lopez", "32/13/2026"))
probar("Devolución", "L01", True, lambda: inv.devolver_equipo(i, "L01"))
probar("Listado por categoría", "L01 devuelto", True,
       lambda: (True, str(inv.contar_disponibles_por_categoria(i))))