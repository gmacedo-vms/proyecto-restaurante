import csv

def validar_usuario(usuario, contrasena):
    with open('data/usuarios.csv', mode='r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila[1] == usuario and fila[2] == contrasena:
                return True
    return False