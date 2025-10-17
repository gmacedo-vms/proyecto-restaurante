from models.detalle_pedido import DetallePedido
from datetime import datetime

class Pedido:
    def __init__(self, pedido_id, mesero_id, mesa_id):
        self.pedido_id = pedido_id
        self.fecha_pedido = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.mesero_id = mesero_id
        self.mesa_id = mesa_id
        self.detalles = []

    def agregar_detalle(self, detalle: DetallePedido):
        self.detalles.append(detalle)

    def calcular_total(self):
        return round(sum(d.subtotal for d in self.detalles), 2)

    def to_dict(self):
        return {
            "pedido_id": self.pedido_id,
            "fecha_pedido": self.fecha_pedido,
            "mesero_id": self.mesero_id,
            "mesa_id": self.mesa_id,
            "total_pedido": f"{self.calcular_total():.2f}"
        }
