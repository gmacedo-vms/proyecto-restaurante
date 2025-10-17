import tkinter as tk

from views.vista_reporte import dibujar_pantalla_reporte
from views.vista_usuarios import dibujar_pantalla_usuarios
from views.vista_platos import dibujar_pantalla_platos

def dibujar_pantalla_administrador(root, resultado):
    texto_bienvenida = f"Bienvenido {resultado.nombre} {resultado.apellidos}"
    texto_rol = f"Rol: {resultado.rol_descripcion}"
    root.lbl_subtitulo.config(text=texto_bienvenida + " - " + texto_rol)

    root.frame_cuerpo = tk.Frame(root, bg='#F54927')
    root.frame_cuerpo.place(relx=0.5, rely=0.15, anchor='n', relwidth=1, relheight=0.85)

    root.col_izquierda = tk.Frame(root.frame_cuerpo, bg='#e6f2ff')
    root.col_izquierda.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)

    root.col_derecha = tk.Frame(root.frame_cuerpo, bg='#e6f2ff')
    root.col_derecha.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)

    lbl_productos = tk.Label(root.col_izquierda, text="Opciones:",
                             font=('Aptos', 16, 'bold'),
                             bg='#e6f2ff', fg='#1a1a1a', padx=10, pady=10)
    lbl_productos.pack(pady=(20, 10), padx=10, anchor='nw')

    # ✅ Lista de botones con texto, acción y colores personalizados
    botones = [
        ("Platos", lambda: dibujar_pantalla_platos(root.col_derecha), "#27AE60",
         "#2ECC71", "white"),  # Verde
        ("Reportes", lambda: dibujar_pantalla_reporte(root.col_derecha), "#2980B9",
         "#3498DB", "white"),  # Azul
        ("Usuarios", lambda: dibujar_pantalla_usuarios(root.col_derecha), "#E67E22",
         "#D35400", "white")  # Naranja
    ]

    for texto, accion, color_bg, color_active, color_fg in botones:
        btn = tk.Button(root.col_izquierda, text=texto, font=('Aptos', 14, 'bold'),
                        bg=color_bg, fg=color_fg,
                        activebackground=color_active, activeforeground=color_fg,
                        relief='flat', bd=0, cursor='hand2',
                        width=15, height=2, command=accion)
        btn.pack(pady=8, padx=10, anchor='nw')

