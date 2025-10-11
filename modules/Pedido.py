import itertools
from datetime import datetime
from .Pedido_Detalle import PedidoDetalle

class Pedido:
    _id_counter = itertools.count(1)

    def __init__(self, cliente) -> None:
        self.id = next(Pedido._id_counter)
        self.detalles = []
        self.cliente = cliente
        self.fecha = datetime.now()

    def agregar_plato(self , plato , cantidad):
        detalle = PedidoDetalle(plato , cantidad)
        self.detalles.append(detalle)

    def calc_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.precio_unitaio * detalle.cantidad
            return total
