import csv
from modules.Plato import Plato


class Menu:
    def __init__(self , platos_csv="data/platos.csv") -> None:
        self.platos = self.cargar_platos(platos_csv)

    def cargar_platos(self , archivo):
        platos = []
        try:
            with open(archivo , mode='r' , encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for fila in csv_reader:
                    _ , nombre , descripcion , precio = fila
                    try:
                        precio = float(precio)
                        plato = Plato(nombre, descripcion , precio)
                        platos.append(plato)
                    except ValueError:
                        print(f"Error: al añadir el plato")

        except FileNotFoundError:
            print(f"Error: El archivo de Platos no fue Encontrado")
            return []
        return platos

    def mostrar_menu(self):
        print("--- MENU DEL RESTAURANTE ---")
        for i , plato in enumerate(self.platos):
            print(f"[{i + 1}] {plato.nombre} - {plato.precio:.2f}")
            print(f"\t{plato.descripcion}")
