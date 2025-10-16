import tkinter as tk
from modules.inicio_sesion import validar_usuario
from views.vista_mesero import dibujar_pantalla_mesero
from views.vista_administrador import dibujar_pantalla_administrador

def dibujar_login(frame_destino, root):
    for widget in frame_destino.winfo_children():
        widget.destroy()

    root.lbl_subtitulo.config(text='Ingrese sus credenciales para continuar')

    # Frame contenedor del formulario centrado
    frame_login = tk.Frame(frame_destino, bg='#e6f2ff')
    frame_login.place(relx=0.5, rely=0.5, anchor='center')

    # Frame interno para centrar los widgets
    formulario = tk.Frame(frame_login, bg='#e6f2ff')
    formulario.pack()

    # 🆕 Texto superior: "Ingrese sus credenciales"
    tk.Label(
        formulario,
        text='Ingrese sus credenciales',
        font=('Aptos', 16, 'bold'),
        bg='#e6f2ff',
        fg='#1a1a1a'
    ).pack(pady=(0, 20))

    tk.Label(formulario, text='Usuario:', font=('Aptos', 14), bg='#e6f2ff',
             fg='#333333').pack(pady=(0, 5))
    usuario_entry = tk.Entry(formulario, font=('Aptos', 14), width=30, bg='white',
                             fg='#333333')
    usuario_entry.pack(pady=(0, 10))

    tk.Label(formulario, text='Clave:', font=('Aptos', 14), bg='#e6f2ff',
             fg='#333333').pack(pady=(0, 5))
    clave_entry = tk.Entry(formulario, font=('Aptos', 14), show='*', width=30,
                           bg='white', fg='#333333')
    clave_entry.pack(pady=(0, 10))

    # 🔴 Label para mostrar errores
    lbl_error = tk.Label(formulario, text='', font=('Aptos', 12), bg='#e6f2ff',
                         fg='#E74C3C')
    lbl_error.pack(pady=(5, 0))

    # Botón de ingreso
    tk.Button(
        formulario,
        text='Ingresar',
        font=('Aptos', 14, 'bold'),
        bg='#E74C3C',
        fg='#ffffff',
        activebackground='#C0392B',
        activeforeground='#ffffff',
        relief='flat',
        bd=0,
        cursor='hand2',
        command=lambda: procesar_login(root, usuario_entry.get(), clave_entry.get(),
                                       lbl_error)
    ).pack(pady=(10, 0))


def procesar_login(root, usuario, clave, lbl_error):
    resultado = validar_usuario(usuario, clave)

    if not resultado:
        lbl_error.config(text='Usuario o clave incorrectos')
    if resultado.rol:
        if resultado.rol == 'mesero':
            dibujar_pantalla_mesero(root, resultado)
        elif resultado.rol == 'admin':
            dibujar_pantalla_administrador(root, resultado)
        else:
            lbl_error.config(text='Rol de usuario no reconocido')

