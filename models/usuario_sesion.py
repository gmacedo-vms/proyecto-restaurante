class UsuarioSesion:
    # Usuario por defecto como variable de clase
    usuario_por_defecto = {
        "identificador": 0,
        "nombre": "Invitado",
        "clave": "1234",
        "correo": "invitado@correo.com",
        "rol": "visitante",
        "estado": "inactivo"
    }

    def __init__(self, identificador=None, nombre=None, clave=None,
                 correo=None, rol=None, estado=None):
        self.identificador = identificador if identificador is not None else \
        UsuarioSesion.usuario_por_defecto["identificador"]
        self.nombre = nombre if nombre is not None else \
        UsuarioSesion.usuario_por_defecto["nombre"]
        self.clave = clave if clave is not None else UsuarioSesion.usuario_por_defecto[
            "clave"]
        self.correo = correo if correo is not None else \
        UsuarioSesion.usuario_por_defecto["correo"]
        self.rol = rol if rol is not None else UsuarioSesion.usuario_por_defecto["rol"]
        self.estado = estado if estado is not None else \
        UsuarioSesion.usuario_por_defecto["estado"]

    @classmethod
    def invitado(cls):
        """Constructor alternativo que retorna un usuario invitado"""
        return cls(
            identificador=cls.usuario_por_defecto["identificador"],
            nombre=cls.usuario_por_defecto["nombre"],
            clave=cls.usuario_por_defecto["clave"],
            correo=cls.usuario_por_defecto["correo"],
            rol=cls.usuario_por_defecto["rol"],
            estado=cls.usuario_por_defecto["estado"]
        )

    def __str__(self):
        return (
            f"UsuarioSesion({self.identificador}): {self.nombre} - {self.rol} "
            f"- Estado: {self.estado}"
        )

    def validar_clave(self, entrada):
        return self.clave == entrada

    def activar(self):
        self.estado = 'activo'

    def desactivar(self):
        self.estado = 'inactivo'
