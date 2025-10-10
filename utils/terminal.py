import os
import platform

def limpiar_consola_alt():
    # Para Windows
    system = platform.system()
    if system == 'Windows':
        _ = os.system('cls')
    # Para macOS y Linux
    else:
        _ = os.system('clear')
