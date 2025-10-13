import csv
from models.usuario_sesion import UsuarioSesion  # Asegúrate de que el path sea correcto

def validar_usuario(usuario, contrasena):
    try:
        with open('data/usuarios.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                # Orden esperado: identificador, nombre, clave, correo, rol, estado
                if fila[1] == usuario and fila[2] == contrasena:
                    return UsuarioSesion(
                        identificador=int(fila[0]),
                        nombre=fila[1],
                        clave=fila[2],
                        correo=fila[3],
                        rol=fila[4],
                        estado=fila[5]
                    )
    except FileNotFoundError:
        print("⚠️ Archivo usuarios.csv no encontrado.")
    except Exception as e:
        print(f"⚠️ Error al validar usuario: {e}")

    # Si no se encuentra el usuario, devuelve None
    return None
