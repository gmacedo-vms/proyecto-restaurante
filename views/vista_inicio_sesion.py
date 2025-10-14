import tkinter as tk
from modules.inicio_sesion import validar_usuario

def dibujar_login(frame_destino):
    for widget in frame_destino.winfo_children():
        widget.destroy()

    # Frame contenedor del formulario centrado
    frame_login = tk.Frame(frame_destino, bg='#e6f2ff')
    frame_login.place(relx=0.5, rely=0.5, anchor='center')

    # Frame interno para centrar los widgets
    formulario = tk.Frame(frame_login, bg='#e6f2ff')
    formulario.pack()

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
        command=lambda: procesar_login(usuario_entry.get(), clave_entry.get())
    ).pack(pady=(10, 0))

def procesar_login(usuario, clave):
    print(f'{usuario}')
    print(validar_usuario(usuario, clave))

    print(f'Usuario: {usuario}, Clave: {clave}')
    # Aquí puedes agregar validación o navegación
