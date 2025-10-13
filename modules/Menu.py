import csv
from modules.Plato import Plato
from utils.styles import Estilos
from utils.terminal import longitud_sin_ansi

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
                    id , nombre , descripcion , precio = fila
                    try:
                        id = int(id)
                        precio = float(precio)
                        plato = Plato(id, nombre, descripcion , precio)
                        platos.append(plato)
                    except ValueError:
                        print(f"Error: al añadir el plato")

        except FileNotFoundError:
            print(f"Error: El archivo de Platos no fue Encontrado")
            return []
        return platos

    def get_platos(self):
        return self.platos

    def mostrar_menu(self , carrito_pedido):
        # carrito_pedido = []
        ancho_menu = 45 
        ancho_pedido = 30
        separacion = 5

        titulo_menu = "MENU DEL RESTAURANTE"
        titulo_pedido = "TU PEDIDO"

        print(f"{Estilos.TITULO}{titulo_menu.center(ancho_menu)}{' '*separacion}{titulo_pedido.center(ancho_pedido)}{Estilos.NORMAL}")
        print(f"{Estilos.TITULO}{'='*ancho_menu}{' '*separacion}{'='*ancho_pedido}{Estilos.NORMAL}")
        print()

        menu_opciones = list(self.platos)
        lineas_pedido = [f"{Estilos.CIAN}- {p.nombre}{Estilos.NORMAL}" for p in carrito_pedido]


        for i in range(max(len(self.platos) , len(carrito_pedido))):
            menu_linea = ""
            if i < len(menu_opciones):
                nombre = self.platos[i].nombre
                precio = self.platos[i].precio
                menu_linea = f"  {Estilos.AMARILLO}[{i + 1}]{Estilos.NORMAL} {nombre:.<20} {Estilos.VERDE}${precio:.2f}{Estilos.NORMAL}"

            pedido_linea = ""
            if i < len(lineas_pedido):
                pedido_linea = lineas_pedido[i]

            espacios_relleno = ancho_menu - longitud_sin_ansi(menu_linea)
            print(f"{menu_linea}{' '*espacios_relleno}{' '*separacion}{pedido_linea}")

        print()
        print(f"{Estilos.ROJO}[0]{Estilos.NORMAL} Finalizar pedido")
        print("------------------------------")

