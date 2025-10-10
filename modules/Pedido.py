from .Pedido_Detalle import PedidoDetalle

class Pedido:
    def __init__(self, cliente) -> None:
        self.detalles = []
        self.cliente = cliente

    def agregar_plato(self , plato , cantidad):
        detalle = PedidoDetalle(plato , cantidad)
        self.detalles.append(detalle)

    def calc_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.precio_unitaio * detalle.cantidad
            return total
