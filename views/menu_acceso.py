from views.vista_inicio_sesion import iniciar_sesion

def mostrar_menu_inicial():

    while True:
        print("\n=== Menú de acceso ===")
        print("1. Inicia sesión")
        print("2. Regístrate")
        print("3. Accede como invitado")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            iniciar_sesion()
            print('opción 1')
        elif opcion == '2':
            print('opción 2')
        elif opcion == '3':
            print('opción 2')
        else:
            print('opcion invalida')
        return opcion
