class Plato:
    def __init__(self, identificador, nombre, descripcion, precio, activo):
        self.identificador = identificador      # Ej: P0001
        self.nombre = nombre                    # Ej: "Spaghetti a la Carbonara"
        self.descripcion = descripcion          # Ej: "Spaghetti con salsa de huevo"
        self.precio = float(precio)             # Ej: 12.50
        self.activo = activo.lower() == "true"  # Convierte "true"/"false" a booleano

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.identificador} - {self.nombre} ({estado}) - S/ {self.precio:.2f}"

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": f"{self.precio:.2f}",
            "activo": "true" if self.activo else "false"
        }
