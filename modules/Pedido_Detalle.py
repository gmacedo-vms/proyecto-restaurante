from .Plato import Plato

class PedidoDetalle:
    def __init__(self, plato: Plato , cantidad: int) -> None:
        self.plato = plato
        self.cantidad = cantidad
        self.precio_unitario = plato.precio

