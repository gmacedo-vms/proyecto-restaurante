from collections import defaultdict
import csv
import os

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data') # -> .../proyecto-restaurante/data/

# Las rutas completas que usarás
PEDIDOS_PATH = os.path.join(DATA_DIR, 'Pedidos.csv')
MENU_PATH = os.path.join(DATA_DIR, 'Menu.csv')
MESEROS_PATH = os.path.join(DATA_DIR, 'Meseros.csv')

def ReporteporFecha():
    # Reporte por fecha
    print("\n1. REPORTE POR FECHA (Cantidad de platos vendidos por día):")
    print("-" * 70)
    
    platos_por_fecha = defaultdict(int)
    
    # Leer el archivo CSV de Pedidos
    #pedidos_path = os.path.join(DATO_DIR, 'Pedidos.csv')
    with open(PEDIDOS_PATH, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter= ';')
        reader.fieldnames = [header.strip() for header in reader.fieldnames]
        for pedido in reader:
            # Limpiar espacios en las claves
            pedido = {k.strip(): v for k, v in pedido.items()}
            fecha = pedido.get('Fecha', '')
            platos_por_fecha[fecha] += 1
    
    for fecha in sorted(platos_por_fecha.keys()):
        print(f"  {fecha}: {platos_por_fecha[fecha]} platos vendidos")





def ReporteporPlato():
    # Reporte por plato
    print("\n2. REPORTE POR PLATO (Cantidad vendida de cada plato):")
    print("-" * 70)
    
    platos_vendidos = defaultdict(int)
        
    # Leer el archivo CSV de Pedidos
    #pedidos_path = os.path.join(DATO_DIR, 'Pedidos.csv')
    with open(PEDIDOS_PATH, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        reader.fieldnames = [header.strip() for header in reader.fieldnames]
        for pedido in reader:
            # Limpiar espacios en las claves
            pedido = {k.strip(): v for k, v in pedido.items()}
            plato_id = int(pedido.get('ID_Plato', pedido.get('ID Plato', 0)))
            platos_vendidos[plato_id] += 1
        
    platos_ordenados = sorted(platos_vendidos.items(), key=lambda x: x[1], reverse=True)
        
    # Leer el menú para obtener los nombres
    menu = {}
    #menu_path = os.path.join(DATO_DIR, 'Menu.csv')
    with open(MENU_PATH, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        reader.fieldnames = [header.strip() for header in reader.fieldnames]
        for plato in reader:
            # Limpiar espacios en las claves
            plato = {k.strip(): v for k, v in plato.items()}
            menu[int(plato['ID'])] = plato['NombreMenu']
        
        for plato_id, cantidad in platos_ordenados:
            plato_nombre = menu.get(plato_id, "Desconocido")
            print(f"  {plato_nombre} (ID: {plato_id}): {cantidad} unidades") 



def ReporteporMesero():
    # Reporte por mesero
    print("\n3. REPORTE POR MESERO (Calificación promedio):")
    print("-" * 70)
    
    calificaciones_meseros = defaultdict(list)

    # Leer el archivo CSV de Pedidos
    pedidos_procesados = set()
    #pedidos_path = os.path.join(DATO_DIR, 'Pedidos.csv')
    with open(PEDIDOS_PATH, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter= ';')
        reader.fieldnames = [header.strip() for header in reader.fieldnames]
        for pedido in reader:
            # Limpiar espacios en las claves
            pedido = {k.strip(): v for k, v in pedido.items()}
            
            id_pedido = pedido.get('ID_Pedido', pedido.get('ID Pedido', ''))
            mesero_id = int(pedido.get('ID_Mesero', pedido.get('ID Mesero', 0)))
            calificacion = int(pedido.get('Calificacion_Mesero', pedido.get('Calificacion Mesero', 0)))
            
            # Evitar contar el mismo pedido múltiples veces
            if id_pedido not in pedidos_procesados:
                calificaciones_meseros[mesero_id].append(calificacion)
                pedidos_procesados.add(id_pedido)
    
    # Leer meseros
    meseros = {}
    #meseros_path = os.path.join(DATO_DIR, 'Meseros.csv')
    with open(MESEROS_PATH, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter= ';')
        reader.fieldnames = [header.strip() for header in reader.fieldnames]
        for mesero in reader:
            # Limpiar espacios en las claves
            mesero = {k.strip(): v for k, v in mesero.items()}
            meseros[int(mesero['ID'])] = mesero['NombreMesero']
    
    meseros_ranking = []
    for mesero_id, calificaciones in calificaciones_meseros.items():
        if calificaciones:
            promedio = sum(calificaciones) / len(calificaciones)
            nombre = meseros.get(mesero_id, "Desconocido")
            meseros_ranking.append((nombre, promedio, len(calificaciones)))
    
    meseros_ranking.sort(key=lambda x: x[1], reverse=True)
    
    if meseros_ranking:
        print(f"\n  🏆 MEJOR MESERO: {meseros_ranking[0][0]}")
        print(f"     Calificación promedio: {meseros_ranking[0][1]:.2f}/5.00")
        print(f"     Total de pedidos atendidos: {meseros_ranking[0][2]}\n")
        
        for nombre, promedio, total in meseros_ranking:
            print(f"  {nombre}: {promedio:.2f}/5.00 ({total} pedidos)")