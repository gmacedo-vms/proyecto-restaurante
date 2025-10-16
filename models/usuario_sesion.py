class UsuarioSesion:
    # Usuario por defecto como variable de clase
    usuario_por_defecto = {
        "identificador": 0,
        "nombre": "Invitado",
        "apellidos": "",
        "usuario": "invitado",
        "clave": "1234",
        "correo": "invitado@correo.com",
        "rol": "visitante",
        "rol_descripcion": "Invitado",
        "activo": False
    }

    def __init__(self, identificador=None, nombre=None, apellidos=None,
                 usuario=None, clave=None, correo=None, rol=None, rol_descripcion= None, activo=None):
        self.identificador = identificador if identificador is not None else self.usuario_por_defecto["identificador"]
        self.nombre = nombre if nombre is not None else self.usuario_por_defecto["nombre"]
        self.apellidos = apellidos if apellidos is not None else self.usuario_por_defecto["apellidos"]
        self.usuario = usuario if usuario is not None else self.usuario_por_defecto["usuario"]
        self.clave = clave if clave is not None else self.usuario_por_defecto["clave"]
        self.correo = correo if correo is not None else self.usuario_por_defecto["correo"]
        self.rol = rol if rol is not None else self.usuario_por_defecto["rol"]
        self.rol_descripcion = rol_descripcion if rol_descripcion is not None else self.usuario_por_defecto["rol_descripcion"]
        self.activo = activo if activo is not None else self.usuario_por_defecto["activo"]

    @classmethod
    def invitado(cls):
        """Constructor alternativo que retorna un usuario invitado"""
        return cls(**cls.usuario_por_defecto)

    def __str__(self):
        estado = "activo" if self.activo else "inactivo"
        return (
            f"UsuarioSesion({self.identificador}): {self.nombre} {self.apellidos} "
            f"- Usuario: {self.usuario} - Rol: {self.rol} "
            f"- Rol_descripcion: {self.rol_descripcion} - Estado: {estado}"
        )

    def validar_clave(self, entrada):
        return self.clave == entrada

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False
