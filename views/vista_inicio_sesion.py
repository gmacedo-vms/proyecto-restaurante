from modules.incio_sesion import validar_usuario
from views.vista_principal import mostrar_menu

import getpass

def iniciar_sesion():

    while True:
        print('\n\n=== Inicio de sesión ===')
        usuario = input('Usuario: ')
        #contrasenia = getpass.getpass('Contraseña: ')
        contrasenia = input('Contraseña: ')

        if validar_usuario(usuario, contrasenia):
            mostrar_menu()
            print('Inicio de sesión exitoso.')
            break
        else:
            print('Usuario o contraseña incorrectos.')
        return False