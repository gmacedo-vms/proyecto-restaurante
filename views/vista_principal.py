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
            menu_principal.mostrar_menu()

    return opcion
