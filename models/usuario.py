class Usuario:
    def __init__(self, identificador, nombre, apellidos, usuario, clave,
                 correo, rol, rol_descripcion, activo):
        self.identificador = identificador
        self.nombre = nombre
        self.apellidos = apellidos
        self.usuario = usuario
        self.clave = clave
        self.correo = correo
        self.rol = rol
        self.rol_descripcion = rol_descripcion
        self.activo = activo.lower() == "true" if isinstance(activo, str) else bool(activo)

    @classmethod
    def from_csv_row(cls, fila):
        return cls(
            identificador=fila["identificador"],
            nombre=fila["nombre"],
            apellidos=fila["apellidos"],
            usuario=fila["usuario"],
            clave=fila["clave"],
            correo=fila["correo"],
            rol=fila["rol"],
            rol_descripcion=fila["rol_descripcion"],
            activo=fila["activo"]
        )

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "usuario": self.usuario,
            "clave": self.clave,
            "correo": self.correo,
            "rol": self.rol,
            "rol_descripcion": self.rol_descripcion,
            "activo": self.activo
        }

    @property
    def es_activo(self):
        return self.activo is True

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.usuario}) - {self.rol_descripcion}"
