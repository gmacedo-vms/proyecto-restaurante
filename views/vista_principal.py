import tkinter as tk
from views.vista_inicio_sesion import dibujar_login
from views.vista_carta import dibujar_menu

def dibujar_pantalla_principal(root):
    root.title('Sistema de Restaurante')
    root.configure(background='#e6f2ff')

    # 🧩 Maximizar ventana
    root.state('zoomed')  # Solo funciona en Windows

    # Dimensiones de pantalla
    root.ancho_pantalla = root.winfo_screenwidth()
    root.alto_pantalla = root.winfo_screenheight()
    root.geometry(f'{root.ancho_pantalla}x{root.alto_pantalla}+0+0')

    # 🧩 Frame superior para el título
    root.frame_titulo = tk.Frame(root, bg='#27AE60')
    root.frame_titulo.place(relx=0.5, rely=0.0, anchor='n', relwidth=1.0, relheight=0.15)

    root.lbl_titulo = tk.Label(
        root.frame_titulo,
        text='Sistema de Gestión de Restaurante',
        font=('Aptos', 32, 'bold'),
        bg='#e6f2ff',
        fg='#1a1a1a'
    )
    root.lbl_titulo.place(relx=0.5, rely=0.5, anchor='center')

    root.lbl_subtitulo = tk.Label(
        root.frame_titulo,
        text='',
        font=('Aptos', 20),
        bg='#e6f2ff',
        fg='#555555'
    )
    root.lbl_subtitulo.place(relx=0.5, rely=0.9, anchor='center')

    # 🧩 Contenedor central
    root.contenedor_central = tk.Frame(root, bg='#e6f2ff')
    root.contenedor_central.place(relx=0.5, rely=0.15, anchor='n', relwidth=1.0, relheight=0.85)

    # 🟦 Columna izquierda
    root.col_izquierda = tk.Frame(root.contenedor_central, bg='#2980B9')
    root.col_izquierda.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

    # 🧩 Contenedor de botones
    root.contenedor_botones = tk.Frame(root.col_izquierda, bg='#e6f2ff')
    root.contenedor_botones.place(relx=0.5, rely=0.5, anchor='center')

    # 🟨 Columna derecha
    root.col_derecha = tk.Frame(root.contenedor_central, bg='#e6f2ff')
    root.col_derecha.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)

    # 🆕 Texto encima del botón “Iniciar sesión”
    root.lbl_indicador_opcion = tk.Label(
        root.contenedor_botones,
        text='Elija una opción',
        font=('Aptos', 16, 'bold'),
        bg='#e6f2ff',
        fg='#333333'
    )
    root.lbl_indicador_opcion.pack(pady=(0, 20))

    # 🔘 Botón 1: Iniciar sesión
    root.btn_inicio = tk.Button(
        root.contenedor_botones,
        text='Iniciar sesión',
        font=('Aptos', 14, 'bold'),
        bg='#27AE60',
        fg='#1a1a1a',
        activebackground='#2ECC71',
        activeforeground='#1a1a1a',
        relief='flat',
        bd=0,
        cursor='hand2',
        command=lambda: dibujar_login(root.col_derecha, root)
    )

    # 🔘 Botón 2: Registrarse
    root.btn_registro = tk.Button(
        root.contenedor_botones,
        text='Registrarse',
        font=('Aptos', 14, 'bold'),
        bg='#2980B9',
        fg='#ffffff',
        activebackground='#3498DB',
        activeforeground='#ffffff',
        relief='flat',
        bd=0,
        cursor='hand2',
        command=lambda: print("Registro")
    )

    # 🔘 Botón 3: Acceder como invitado
    root.btn_salir = tk.Button(
        root.contenedor_botones,
        text='Acceder como invitado',
        font=('Aptos', 14, 'bold'),
        bg='#E74C3C',
        fg='#ffffff',
        activebackground='#C0392B',
        activeforeground='#ffffff',
        relief='flat',
        bd=0,
        cursor='hand2',
        command=lambda: dibujar_menu(root.col_derecha, root)
    )

    # 🧠 Hover para cada botón
    def hover_estilo(widget, color_hover, color_normal):
        widget.bind('<Enter>', lambda e: widget.config(bg=color_hover, font=('Aptos', 14, 'bold', 'underline')))
        widget.bind('<Leave>', lambda e: widget.config(bg=color_normal, font=('Aptos', 14, 'bold')))

    hover_estilo(root.btn_inicio, '#58D68D', '#27AE60')
    hover_estilo(root.btn_registro, '#5DADE2', '#2980B9')
    hover_estilo(root.btn_salir, '#EC7063', '#E74C3C')

    # 🧩 Posicionar los botones
    for boton in [root.btn_inicio, root.btn_registro, root.btn_salir]:
        boton.config(width=20, height=2)
        boton.pack(pady=10, ipadx=20, ipady=10)
