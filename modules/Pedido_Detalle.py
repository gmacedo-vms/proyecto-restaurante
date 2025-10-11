import itertools
from .Plato import Plato

class PedidoDetalle:
    _id_counter = itertools.count(1)

    def __init__(self, plato: Plato , cantidad: int) -> None:
        self.id = next(PedidoDetalle._id_counter)
        self.plato = plato
        self.cantidad = cantidad
        self.precio_unitario = plato.precio

