import tkinter as tk


def dibujar_pantalla_administrador(root, resultado):
    texto_bienvenida = 'Bienvenido ' + resultado.nombre + ' ' + resultado.apellidos
    texto_rol = 'Rol: ' + resultado.rol_descripcion
    root.lbl_subtitulo.config(text=texto_bienvenida + ' - ' + texto_rol)

    root.frame_unificado = tk.Frame(root, bg='#2980B9')
    root.frame_unificado.place(relx=0.5, rely=0.15, anchor='n', relwidth=1,
                               relheight=0.85)

    root.contenedor_central = tk.Frame(root, bg='#2980B9')
    root.contenedor_central.place(relx=0.5, rely=0.15, anchor='n', relwidth=1.0,
                                  relheight=0.85)

    # Luego colocas los widgets de col_izquierda y col_derecha dentro de frame_unificado
    # 🔘 Botón 1: Iniciar sesión
    root.btn_inicio = tk.Button(
        root.contenedor_central,
        text='Iniciar sesión',
        font=('Aptos', 14, 'bold'),
        bg='#27AE60',
        fg='#1a1a1a',
        activebackground='#2ECC71',
        activeforeground='#1a1a1a',
        relief='flat',
        bd=0,
        cursor='hand2'
    )

    for boton in [root.btn_inicio]:
        boton.config(width=20, height=2)
        boton.pack(pady=10, ipadx=20, ipady=10)

    print(resultado.rol)
    pass
