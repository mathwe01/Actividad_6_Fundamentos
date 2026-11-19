import inventario  as inv

def mostrar_menu():
    print("\n--- LABTECH: PRÉSTAMO DE EQUIPOS ---")
    print("1. Registrar equipo")
    print("2. Prestar equipo")
    print("3. Devolver equipo")
    print("4. Listar equipos que esten disponibles")
    print("5. Disponibles por categoría")
    print("0. Salir")
    
def accion_registrar(inventario):
    ok, msg = inv.registrar_equipo(inventario, input("Código: "),
                                   input("Nombre: "), input("Categoria: "))
    print(msg)
    
def accion_prestar(inventario, prestamos):
    ok, msg = inv.prestar_equipo(inventario, prestamos, input("Codigo "),
                                 input("Estudiante "), input("Fecha (dd/mm/yyyy): "))
    print(msg)
    
def accion_devolver(inventario):
    print(inv.devolver_equipo(inventario, input("Código: "))[1])

def accion_listar(inventario):
    disponibles = inv.listar_disponibles(inventario)
    if not disponibles:
        print("No hay equipos disponibles.")
    for codigo, d in disponibles:
        print(f"{codigo} | {d['nombre']} | {d['categoria']}")
        
def accion_por_categoria(inventario):
    conteo = inv.contar_disponibles_por_categoria(inventario)
    if not conteo:
        print("No hay equipos disponibles.")
    for categoria, cantidad in conteo.items():
        print(f"{categoria}: {cantidad}")
        
def main():
    inventario, prestamos = inv.crear_inventario(), []
    while True:
        mostrar_menu()
        opcion = input("Opcion ").strip()
        if opcion == "1":
            accion_registrar(inventario)
        elif opcion == "2":
            accion_prestar(inventario, prestamos)
        elif opcion == "3":
            accion_devolver(inventario)
        elif opcion == "4":
            accion_listar(inventario)
        elif opcion == "5":
            accion_por_categoria(inventario)
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opcion no válida")
            


if __name__ == "__main__":
    main()

            
            
        
    