import tkinter as tk

platos_menu = [
    {'nombre': 'Lomo Saltado', 'precio': 18.0},
    {'nombre': 'Ceviche Mixto', 'precio': 22.0},
    {'nombre': 'Aji de Gallina', 'precio': 16.0},
    {'nombre': 'Pollo a la Brasa', 'precio': 20.0}
]

def dibujar_menu(frame_destino, root):
    for widget in frame_destino.winfo_children():
        widget.destroy()

    frame_menu = tk.Frame(frame_destino, bg='#e6f2ff')
    frame_menu.place(relx=0.5, rely=0.5, anchor='center')

    formulario = tk.Frame(frame_menu, bg='#e6f2ff')
    formulario.pack()

    tk.Label(formulario, text='Seleccione sus platos:', font=('Aptos', 16, 'bold'), bg='#e6f2ff').pack(pady=10)

    seleccionados = {}

    for plato in platos_menu:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(
            formulario,
            text=f"{plato['nombre']} - S/ {plato['precio']:.2f}",
            variable=var,
            font=('Aptos', 14),
            bg='#e6f2ff',
            anchor='w'
        )
        chk.pack(fill='x', padx=20, pady=5)
        seleccionados[plato['nombre']] = var

    # 🔘 Botón para confirmar pedido
    def confirmar_pedido():
        pedido = [nombre for nombre, var in seleccionados.items() if var.get()]
        total = sum(plato['precio'] for plato in platos_menu if plato['nombre'] in pedido)

        print("Pedido:", pedido)
        print("Total: S/", total)

        lbl_resultado.config(text=f"Pedido: {', '.join(pedido)}\nTotal: S/ {total:.2f}")

    tk.Button(
        formulario,
        text='Confirmar Pedido',
        font=('Aptos', 14, 'bold'),
        bg='#27AE60',
        fg='white',
        relief='flat',
        bd=0,
        cursor='hand2',
        command=confirmar_pedido
    ).pack(pady=15)

    lbl_resultado = tk.Label(formulario, text='', font=('Aptos', 12), bg='#e6f2ff', fg='#1a1a1a')
    lbl_resultado.pack(pady=10)
