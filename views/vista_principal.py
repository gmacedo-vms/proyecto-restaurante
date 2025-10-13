from utils.styles import Estilos
from utils.terminal import limpiar_consola_alt
from modules.Menu import Menu

def mostrar_menu():
    limpiar_consola_alt()
    print("\n\n=== Menú Principal ===")
    print("1. Ver la carta")
    print("2. Ver los descuentos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case '1':
            limpiar_consola_alt()

            menu_principal = Menu()
            carrito_pedido = []
            platos = menu_principal.get_platos()
            while True:
                menu_principal.mostrar_menu(carrito_pedido)

                opcion = input(f"{Estilos.BLANCO}ELije una opcion: {Estilos.NORMAL}").strip()

                if opcion == "0":
                    break

                if opcion != '0' and opcion.isnumeric():
                    plato_elegido = platos[int(opcion) - 1]
                    carrito_pedido.append(plato_elegido)
                else:
                    pass

            limpiar_consola_alt()

    return opcion
