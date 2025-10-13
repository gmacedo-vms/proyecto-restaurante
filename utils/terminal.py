import os
import re
import platform

def limpiar_consola_alt():
    # Para Windows
    system = platform.system()
    if system == 'Windows':
        _ = os.system('cls')
    # Para macOS y Linux
    else:
        _ = os.system('clear')


def longitud_sin_ansi(cadena):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return len(ansi_escape.sub('', cadena))
