import tkinter as tk
from tkinter import messagebox
from models.usuario import Usuario
from modules.usuarios import agregar_usuario, buscar_usuario_por_nombre
from modules.inicio_sesion import validar_usuario
from views.vista_carta import dibujar_vista_carta

def dibujar_registro(frame_destino, root):
    for widget in frame_destino.winfo_children():
        widget.destroy()

    root.lbl_subtitulo.config(text='Registro de nuevo usuario')

    frame_registro = tk.Frame(frame_destino, bg='#e6f2ff')
    frame_registro.place(relx=0.5, rely=0.05, anchor='n')  # ✅ Elevado arriba

    formulario = tk.Frame(frame_registro, bg='#e6f2ff')
    formulario.pack(anchor='nw', padx=30, pady=20)  # ✅ Alineado a la izquierda con margen

    campos = {}

    def agregar_placeholder(entry, texto):
        entry.insert(0, texto)
        entry.config(fg='gray')

        def limpiar(event):
            if entry.get() == texto:
                entry.delete(0, 'end')
                entry.config(fg='black')

        def restaurar(event):
            if not entry.get():
                entry.insert(0, texto)
                entry.config(fg='gray')

        entry.bind("<FocusIn>", limpiar)
        entry.bind("<FocusOut>", restaurar)

    for label_text in ["Identificador", "Nombre", "Apellidos", "Usuario", "Clave", "Correo"]:
        fila = tk.Frame(formulario, bg='#e6f2ff')
        fila.pack(fill='x', pady=10)

        lbl = tk.Label(fila, text=label_text + ":", font=('Aptos', 14), bg='#e6f2ff',
                       anchor='w', width=15)
        lbl.pack(side='left', padx=(0, 15))

        if label_text.lower() == "clave":
            entry = tk.Entry(fila, font=('Aptos', 14), width=30, bg='white', show='*')  # ✅ Oculta clave
        else:
            entry = tk.Entry(fila, font=('Aptos', 14), width=30, bg='white')

        entry.pack(side='right', padx=(15, 0))
        agregar_placeholder(entry, f"Ingrese {label_text.lower()}")
        campos[label_text.lower()] = entry

    lbl_error = tk.Label(formulario, text='', font=('Aptos', 14), bg='#f9f9f9', fg='#E74C3C')
    lbl_error.pack(pady=20)

    def registrar():
        valores = {campo: entry.get().strip() for campo, entry in campos.items()}

        # Validar campos obligatorios
        campos_vacios = [nombre for nombre, valor in valores.items()
                         if not valor or valor.startswith("Ingrese ")]
        if campos_vacios:
            lbl_error.config(
                text=f"⚠️ Los siguientes campos son obligatorios: {', '.join(campos_vacios)}")
            return

        if buscar_usuario_por_nombre(valores["usuario"]):
            lbl_error.config(text="⚠️ El usuario ya existe")
            return

        nuevo = Usuario(
            identificador=valores["identificador"],
            nombre=valores["nombre"],
            apellidos=valores["apellidos"],
            usuario=valores["usuario"],
            clave=valores["clave"],
            correo=valores["correo"],
            rol="cliente",
            rol_descripcion="Cliente del restaurante",
            activo=True
        )

        agregar_usuario(nuevo)

        respuesta = messagebox.askquestion(
            "Registro exitoso",
            "✅ El usuario ha sido registrado correctamente.\n\n¿Deseas ir al menú de cartas ahora?",
            icon='info'
        )

        if respuesta == 'yes':
            usuario_logueado = validar_usuario(nuevo.usuario, nuevo.clave)
            if usuario_logueado and usuario_logueado.rol == "cliente":
                dibujar_vista_carta(root, usuario_logueado)
            else:
                messagebox.showerror("Error",
                                     "No se pudo iniciar sesión automáticamente.")
        else:
            messagebox.showinfo("Registro finalizado",
                                "Puedes iniciar sesión más tarde desde el menú principal.")

    btn_registrar = tk.Button(formulario, text='Registrar', font=('Aptos', 14, 'bold'),
        bg='#27AE60', fg='white', padx=10, pady=5,
        activebackground='#229954', cursor='hand2',
        command=registrar)
    btn_registrar.pack(pady=(10, 30))  # ✅ Separación inferior de 30px

    # ✅ Beneficios destacados tras el botón
    beneficios = [
        "🎁 Acceso a promociones exclusivas",
        "💸 Descuentos especiales en tus pedidos",
        "📊 Reportes detallados de tu historial",
        "** Atención personalizada como cliente registrado",
        "📬 Notificaciones de novedades y eventos"
    ]

    for texto in beneficios:
        lbl_beneficio = tk.Label(formulario, text=texto, font=('Aptos', 14),
                                 bg='#e6f2ff', fg='#2E86C1', anchor='w')
        lbl_beneficio.pack(fill='x', padx=10, pady=15)
