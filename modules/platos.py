import csv
import os
from models.plato import Plato  # Asegúrate de que el path sea correcto

ruta_base = os.path.dirname(__file__)
ruta_csv = os.path.join(ruta_base, '..', 'data', 'platos.csv')

def listar_platos():
    lista = []

    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if all([fila['identificador'], fila['nombre'], fila['descripcion'], fila['precio']]):
                    plato = Plato(
                        identificador=fila['identificador'],
                        nombre=fila['nombre'],
                        descripcion=fila['descripcion'],
                        precio=fila['precio'],
                        activo=fila['activo']
                    )
                    lista.append(plato)
    except FileNotFoundError:
        print("❌ Archivo platos.csv no encontrado.")
    except Exception as e:
        print(f"⚠️ Error al leer platos: {e}")

    return lista

def inactivar_plato(identificador):
    actualizado = False
    platos_actualizados = []

    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila['identificador'] == identificador:
                    fila['activo'] = "false"
                    actualizado = True
                platos_actualizados.append(fila)

        if actualizado:
            campos = ['identificador', 'nombre', 'descripcion', 'precio', 'activo']
            with open(ruta_csv, mode='w', encoding='utf-8', newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(platos_actualizados)
        else:
            raise Exception(f"No se encontró el plato con ID '{identificador}'.")

    except Exception as e:
        raise Exception(f"Error al inactivar plato: {e}")

def agregar_plato(datos):
    campos = ['identificador', 'nombre', 'descripcion', 'precio', 'activo']
    try:
        with open(ruta_csv, mode='a', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writerow(datos)
    except Exception as e:
        raise Exception(f"Error al guardar plato: {e}")

def obtener_siguiente_id_plato():
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            ultimos_ids = [fila['identificador'] for fila in lector if fila.get('identificador', '').startswith('P')]

        if not ultimos_ids:
            return "P0001"

        # Extraer el número y encontrar el máximo
        max_num = max(int(id[1:]) for id in ultimos_ids)
        siguiente_num = max_num + 1
        return f"P{siguiente_num:04d}"

    except FileNotFoundError:
        return "P0001"
    except Exception as e:
        raise Exception(f"Error al generar el siguiente ID: {e}")
