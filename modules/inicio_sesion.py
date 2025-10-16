import csv
import os
from models.usuario_sesion import UsuarioSesion  # Asegúrate de que el path sea correcto

ruta_base = os.path.dirname(__file__)
ruta_csv = os.path.join(ruta_base, '..', 'data', 'usuarios.csv')

def validar_usuario(usuario, contrasena):
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Usa encabezados como claves
            for fila in lector:
                if fila['usuario'] == usuario and fila['clave'] == contrasena:
                    return UsuarioSesion(
                        identificador=int(fila['identificador']),
                        nombre=fila['nombre'],
                        apellidos=fila['apellidos'],
                        usuario=fila['usuario'],
                        clave=fila['clave'],
                        correo=fila['correo'],
                        rol=fila['rol'],
                        rol_descripcion=fila['rol_descripcion'],
                        activo=fila['activo'].strip().lower() == 'true'
                    )
    except FileNotFoundError:
        print("⚠️ Archivo usuarios.csv no encontrado.")
    except Exception as e:
        print(f"⚠️ Error al validar usuario: {e}")

    return None
