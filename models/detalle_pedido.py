class DetallePedido:
    def __init__(self, nombre_plato, descripcion_plato, precio_unitario, cantidad):
        self.nombre_plato = nombre_plato
        self.descripcion_plato = descripcion_plato
        self.precio_unitario = float(precio_unitario)
        self.cantidad = int(cantidad)
        self.subtotal = round(self.precio_unitario * self.cantidad, 2)

    def to_dict(self, pedido_id):
        return {
            "pedido_id": pedido_id,
            "nombre_plato": self.nombre_plato,
            "descripcion_plato": self.descripcion_plato,
            "precio_unitario": f"{self.precio_unitario:.2f}",
            "cantidad": self.cantidad,
            "subtotal": f"{self.subtotal:.2f}"
        }
