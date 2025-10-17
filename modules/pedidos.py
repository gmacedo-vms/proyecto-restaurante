import csv
import os
from datetime import datetime
from models.pedido import Pedido
from models.detalle_pedido import DetallePedido

# 📂 Rutas blindadas
ruta_base = os.path.dirname(__file__)
ruta_data = os.path.abspath(os.path.join(ruta_base, '..', 'data'))

RUTA_PEDIDOS = os.path.join(ruta_data, 'pedidos.csv')
RUTA_DETALLES = os.path.join(ruta_data, 'detalle_pedidos.csv')

# 📝 Escribir fila en CSV con salto de línea correcto
def escribir_csv(ruta, fila_dict, encabezado):
    escribir_encabezado = not os.path.exists(ruta) or os.stat(ruta).st_size == 0
    with open(ruta, mode="a", encoding="utf-8", newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=encabezado)
        if escribir_encabezado:
            writer.writeheader()
        writer.writerow(fila_dict)

# 🆔 Generar nuevo ID de pedido
def generar_nuevo_id():
    try:
        with open(RUTA_PEDIDOS, mode='r', encoding='utf-8-sig') as archivo:
            lector = csv.DictReader(archivo)
            ids = []
            for fila in lector:
                pid = fila.get('pedido_id', '').strip()
                if pid.startswith('PED'):
                    ids.append(pid)

        if not ids:
            return "PED001"

        max_num = max(int(pid[3:]) for pid in ids)
        siguiente_num = max_num + 1
        return f"PED{siguiente_num:03d}"

    except FileNotFoundError:
        return "PED001"
    except Exception as e:
        raise Exception(f"Error al generar el siguiente ID de pedido: {e}")

# 🟢 Guardar pedido completo (cabecera + detalle)
def guardar_pedido(platos_elegidos, mesero_id, mesa_id):
    pedido_id = generar_nuevo_id()
    pedido = Pedido(pedido_id, mesero_id, mesa_id)

    for nombre, descripcion, precio, cantidad in platos_elegidos:
        detalle = DetallePedido(nombre, descripcion, float(precio), int(cantidad))
        pedido.agregar_detalle(detalle)

    # Guardar cabecera
    escribir_csv(RUTA_PEDIDOS, pedido.to_dict(), encabezado=[
        "pedido_id", "fecha_pedido", "mesero_id", "mesa_id", "total_pedido"
    ])

    # Guardar detalles
    for detalle in pedido.detalles:
        escribir_csv(RUTA_DETALLES, detalle.to_dict(pedido_id), encabezado=[
            "pedido_id", "nombre_plato", "descripcion_plato", "precio_unitario", "cantidad", "subtotal"
        ])

    return pedido_id
