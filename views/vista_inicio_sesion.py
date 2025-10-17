import tkinter as tk
from modules.inicio_sesion import validar_usuario
from views.vista_carta import dibujar_vista_carta
from views.vista_mesero import dibujar_pantalla_mesero
from views.vista_administrador import dibujar_pantalla_administrador

def dibujar_login(frame_destino, root):
    for widget in frame_destino.winfo_children():
        widget.destroy()

    root.lbl_subtitulo.config(text='Ingrese sus credenciales')  # ❌ Eliminar subtítulo

    # Frame contenedor del formulario alineado arriba
    frame_login = tk.Frame(frame_destino, bg='#e6f2ff')
    frame_login.place(relx=0.5, rely=0.05, anchor='n')  # 📍 Alineado arriba

    formulario = tk.Frame(frame_login, bg='#e6f2ff')
    formulario.pack(anchor='nw', padx=30, pady=20)

    # Campos: Usuario y Clave
    fila_usuario = tk.Frame(formulario, bg='#e6f2ff')
    fila_usuario.pack(fill='x', pady=10)

    lbl_usuario = tk.Label(fila_usuario, text='Usuario:', font=('Aptos', 14),
                           bg='#e6f2ff', fg='#333333', width=12, anchor='w')
    lbl_usuario.pack(side='left', padx=(0, 15))

    usuario_entry = tk.Entry(fila_usuario, font=('Aptos', 14), width=30,
                             bg='white', fg='#333333')
    usuario_entry.pack(side='right', padx=(15, 0))

    fila_clave = tk.Frame(formulario, bg='#e6f2ff')
    fila_clave.pack(fill='x', pady=10)

    lbl_clave = tk.Label(fila_clave, text='Clave:', font=('Aptos', 14),
                         bg='#e6f2ff', fg='#333333', width=12, anchor='w')
    lbl_clave.pack(side='left', padx=(0, 15))

    clave_entry = tk.Entry(fila_clave, font=('Aptos', 14), show='*', width=30,
                           bg='white', fg='#333333')
    clave_entry.pack(side='right', padx=(15, 0))

    # 🔴 Label para mostrar errores
    lbl_error = tk.Label(formulario, text='', font=('Aptos', 12),
                         bg='#e6f2ff', fg='#E74C3C')
    lbl_error.pack(pady=(10, 0))

    # Botón de ingreso
    btn_ingresar = tk.Button(formulario, text='Ingresar', font=('Aptos', 14, 'bold'),
                             bg='#27AE60', fg='white', padx=10, pady=5,
                             activebackground='#229954', cursor='hand2',
                             command=lambda: procesar_login(root, usuario_entry.get(),
                                                            clave_entry.get(),
                                                            lbl_error))
    btn_ingresar.pack(pady=(10, 30))  # ✅ Separación inferior de 30px

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

def procesar_login(root, usuario, clave, lbl_error):
    resultado = validar_usuario(usuario, clave)
    print(resultado)
    if not resultado:
        lbl_error.config(text='Usuario o clave incorrectos')
    if resultado.rol:
        if resultado.rol == 'mesero':
            dibujar_pantalla_mesero(root, resultado)
        elif resultado.rol == 'admin':
            dibujar_pantalla_administrador(root, resultado)
        elif resultado.rol == 'cliente':
            dibujar_vista_carta(root, resultado)
        else:
            lbl_error.config(text='Rol de usuario no reconocido')
