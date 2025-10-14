import tkinter as tk
from views.vista_inicio_sesion import dibujar_login

# Crear ventana principal en pantalla completa
root = tk.Tk()
root.title('Sistema de Restaurante')
root.configure(background='#e6f2ff')

# Obtener dimensiones de pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
root.geometry(f'{ancho_pantalla}x{alto_pantalla}+0+0')

# 🧩 Frame superior para el título (pegado arriba)
frame_titulo = tk.Frame(root, bg='#e6f2ff')
frame_titulo.place(relx=0.5, rely=0.0, anchor='n', relwidth=0.8, relheight=0.1)

lbl_titulo = tk.Label(
    frame_titulo,
    text='Sistema de Gestión de Restaurante',
    font=('Aptos', 32, 'bold'),
    bg='#e6f2ff',
    fg='#1a1a1a'
)
lbl_titulo.place(relx=0.5, rely=0.5, anchor='center')

# 🧩 Contenedor central elevado
contenedor_central = tk.Frame(root, bg='#e6f2ff')
contenedor_central.place(relx=0.5, rely=0.45, anchor='center', relwidth=0.8,
                         relheight=0.6)

# 🟦 Columna izquierda
col_izquierda = tk.Frame(contenedor_central, bg='#e6f2ff')
col_izquierda.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

# 🧩 Contenedor vertical para los botones
contenedor_botones = tk.Frame(col_izquierda, bg='#e6f2ff')
contenedor_botones.place(relx=0.5, rely=0.5, anchor='center')

# 🔘 Botón 1: Inicio sesión
btn_inicio = tk.Button(
    contenedor_botones,
    text='Iniciar sesión',
    font=('Aptos', 14, 'bold'),
    bg='#27AE60',
    fg='#1a1a1a',
    activebackground='#2ECC71',
    activeforeground='#1a1a1a',
    relief='flat',
    bd=0,
    cursor='hand2',
    command=lambda: dibujar_login(col_derecha)
)

# 🔘 Botón 2: Registrarse
btn_registro = tk.Button(
    contenedor_botones,
    text='Registrarse',
    font=('Aptos', 14, 'bold'),
    bg='#2980B9',
    fg='#ffffff',
    activebackground='#3498DB',
    activeforeground='#ffffff',
    relief='flat',
    bd=0,
    cursor='hand2',
    command=lambda: print("Registro")  # Reemplaza con tu función real
)

# 🔘 Botón 3: Salir
btn_salir = tk.Button(
    contenedor_botones,
    text='Acceder como invitado',
    font=('Aptos', 14, 'bold'),
    bg='#E74C3C',
    fg='#ffffff',
    activebackground='#C0392B',
    activeforeground='#ffffff',
    relief='flat',
    bd=0,
    cursor='hand2',
    command=root.quit
)


# 🧠 Hover para cada botón
def hover_estilo(widget, color_hover, color_normal):
    widget.bind('<Enter>', lambda e: widget.config(bg=color_hover,
                                                   font=('Aptos', 14, 'bold',
                                                         'underline')))
    widget.bind('<Leave>',
                lambda e: widget.config(bg=color_normal, font=('Aptos', 14, 'bold')))


hover_estilo(btn_inicio, '#58D68D', '#27AE60')
hover_estilo(btn_registro, '#5DADE2', '#2980B9')
hover_estilo(btn_salir, '#EC7063', '#E74C3C')

# 🧩 Posicionar los botones verticalmente con tamaño uniforme
for boton in [btn_inicio, btn_registro, btn_salir]:
    boton.config(width=20, height=2)
    boton.pack(pady=10, ipadx=20, ipady=10)

# 🟨 Columna derecha
col_derecha = tk.Frame(contenedor_central, bg='#e6f2ff')
col_derecha.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)

# Ejecutar ventana
root.mainloop()
