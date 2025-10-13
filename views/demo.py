import tkinter as tk

# Crear ventana principal en pantalla completa
root = tk.Tk()
root.title('Aplicación Principal')
root.configure(background='#e6f2ff')

# Obtener dimensiones de pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
root.geometry(f'{ancho_pantalla}x{alto_pantalla}+0+0')

# 🧩 Contenedor central que ocupa parte proporcional de la pantalla
contenedor_central = tk.Frame(root, bg='#e6f2ff')
contenedor_central.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8, relheight=0.6)

# 🟦 Columna izquierda: ocupa 50% del ancho del contenedor
col_izquierda = tk.Frame(contenedor_central, bg='#e6f2ff')
col_izquierda.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

btn_inicio = tk.Button(
    col_izquierda,
    text='Inicio sesión',
    font=('Aptos', 14),
    bg='#b3d9ff',
    fg='#1a1a1a',
    activebackground='#cce6ff',
    activeforeground='#1a1a1a',
    command=lambda: mostrar_login(col_derecha)
)
btn_inicio.place(relx=0.5, rely=0.5, anchor='center')  # Centrado dinámicamente

# 🟨 Columna derecha: ocupa el otro 50% del ancho
col_derecha = tk.Frame(contenedor_central, bg='#e6f2ff')
col_derecha.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)

# Función para mostrar login (solo se ejecuta al presionar el botón)
def mostrar_login(col_derecha):
    for widget in col_derecha.winfo_children():
        widget.destroy()

    # Frame contenedor del formulario centrado
    frame_login = tk.Frame(col_derecha, bg='#f0f4f8')
    frame_login.place(relx=0.5, rely=0.5, anchor='center')

    # Frame interno para centrar los widgets
    formulario = tk.Frame(frame_login, bg='#f0f4f8')
    formulario.pack()

    tk.Label(formulario, text='Usuario:', font=('Aptos', 12), bg='#f0f4f8', fg='#333333').pack(pady=(0, 5))
    usuario_entry = tk.Entry(formulario, font=('Aptos', 12), width=30, bg='white', fg='#333333')
    usuario_entry.pack(pady=(0, 10))

    tk.Label(formulario, text='Clave:', font=('Aptos', 12), bg='#f0f4f8', fg='#333333').pack(pady=(0, 5))
    clave_entry = tk.Entry(formulario, font=('Aptos', 12), show='*', width=30, bg='white', fg='#333333')
    clave_entry.pack(pady=(0, 10))

    def procesar_login():
        usuario = usuario_entry.get()
        clave = clave_entry.get()
        print(f'Usuario: {usuario}, Clave: {clave}')
        # Aquí puedes agregar validación o navegación

    tk.Button(
        formulario,
        text='Ingresar',
        font=('Aptos', 12),
        bg='#a3d5ff',
        fg='#1a1a1a',
        activebackground='#cce6ff',
        activeforeground='#1a1a1a',
        command=procesar_login
    ).pack(pady=(10, 0))

# Ejecutar la aplicación
root.mainloop()