import itertools
from datetime import datetime
from typing import Optional

from .Pedido_Detalle import PedidoDetalle

class Pedido:
    _id_counter = itertools.count(1)

    def __init__(self, cliente: Optional[Cliente] = None , nombre_invitado: Optional[str] = None) -> None:
        self.id = next(Pedido._id_counter)
        self.detalles = []
        self.fecha = datetime.now()

        if cliente is not None:
            self.cliente = cliente
            self.nombre_invitado = None

        else:
            self.cliente = None
            if nombre_invitado is not None:
                self.nombre_invitado = nombre_invitado
            else:
                self.nombre_invitado = "nombre no proporcionado"

    def get_nombre_cliente(self) -> str:
        if self.cliente:
            return self.cliente.nombre
        else:
            self.nombre_invitado

    def agregar_plato(self , plato , cantidad):
        detalle = PedidoDetalle(plato , cantidad)
        self.detalles.append(detalle)

    def calc_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.precio_unitaio * detalle.cantidad
            return total
