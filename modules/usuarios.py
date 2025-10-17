import csv
import os
from models.usuario_sesion import UsuarioSesion  # Asegúrate de que el path sea correcto
from models.usuario import Usuario

ruta_base = os.path.dirname(__file__)
ruta_csv = os.path.join(ruta_base, '..', 'data', 'usuarios.csv')

def listar_usuarios():
    usuarios = []
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuario = UsuarioSesion(
                    identificador=fila['identificador'],
                    nombre=fila['nombre'],
                    apellidos=fila['apellidos'],
                    usuario=fila['usuario'],
                    clave=fila['clave'],
                    correo=fila['correo'],
                    rol=fila['rol'],
                    rol_descripcion=fila['rol_descripcion'],
                    activo=fila['activo'].strip().lower() == 'true'
                )
                usuarios.append(usuario)
    except FileNotFoundError:
        print("⚠️ Archivo usuarios.csv no encontrado.")
    except Exception as e:
        print(f"⚠️ Error al listar usuarios: {e}")

    return usuarios

def inactivar_usuario(usuario_objetivo):
    usuarios_actualizados = []
    encontrado = False

    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila['usuario'] == usuario_objetivo:
                    fila['activo'] = 'false'
                    encontrado = True
                usuarios_actualizados.append(fila)

        if encontrado:
            with open(ruta_csv, mode='w', encoding='utf-8', newline='') as archivo:
                campos = ['identificador', 'nombre', 'apellidos', 'usuario', 'clave',
                          'correo', 'rol', 'rol_descripcion', 'activo']
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(usuarios_actualizados)
            print(f"🟡 Usuario '{usuario_objetivo}' ha sido inactivado.")
        else:
            print(f"⚠️ Usuario '{usuario_objetivo}' no encontrado.")

    except FileNotFoundError:
        print("❌ Archivo usuarios.csv no encontrado.")
    except Exception as e:
        print(f"⚠️ Error al inactivar usuario: {e}")

def agregar_usuario(usuario: Usuario):
    with open(ruta_csv, "a", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=[
            "identificador", "nombre", "apellidos", "usuario", "clave",
            "correo", "rol", "rol_descripcion", "activo"
        ])
        writer.writerow(usuario.to_dict())

def buscar_usuario_por_nombre(nombre_usuario, ruta_csv="usuarios.csv"):
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["usuario"].strip().lower() == nombre_usuario.strip().lower():
                    return Usuario.from_csv_row(fila)
    except FileNotFoundError:
        print(f"⚠️ Archivo no encontrado: {ruta_csv}")
    except Exception as e:
        print(f"⚠️ Error al buscar usuario: {e}")
    return None
