import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from modules.platos import listar_platos, agregar_plato, inactivar_plato, obtener_siguiente_id_plato

# 🟢 Acción: Agregar plato
def agregar_plato_ui(frame_derecho):
    ventana = Toplevel()
    ventana.title("Agregar Plato")
    ventana.configure(bg='white')

    # 📐 Tamaño base + 20% vertical y centrado
    ancho = 400
    alto = int(400 * 1.2)
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    campos = {
        "ID": StringVar(value=obtener_siguiente_id_plato()),
        "Nombre": StringVar(),
        "Descripción": StringVar(),
        "Precio": StringVar()
    }

    for idx, (label, var) in enumerate(campos.items()):
        Label(ventana, text=label, bg='white', font=('Aptos', 12)).pack(pady=(10 if idx == 0 else 5, 0))
        if label == "ID":
            Entry(ventana, textvariable=var, font=('Aptos', 12), state="readonly").pack()
        else:
            Entry(ventana, textvariable=var, font=('Aptos', 12)).pack()

    def confirmar():
        datos = {
            "identificador": campos["ID"].get(),
            "nombre": campos["Nombre"].get(),
            "descripcion": campos["Descripción"].get(),
            "precio": campos["Precio"].get(),
            "activo": "true"
        }

        if not all([datos[k] for k in ["identificador", "nombre", "descripcion", "precio"]]):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        try:
            float(datos["precio"])
        except ValueError:
            messagebox.showerror("Precio inválido", "El precio debe ser un número válido.")
            return

        try:
            agregar_plato(datos)
            messagebox.showinfo("Plato agregado", f"✅ Plato '{datos['nombre']}' guardado correctamente.")
            ventana.destroy()
            dibujar_pantalla_platos(frame_derecho)  # 🔁 Actualiza la tabla
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(ventana, text="Guardar", font=('Aptos', 12), bg='#27AE60', fg='white',
           padx=10, pady=5, command=confirmar).pack(pady=20)

# 🟡 Acción: Deshabilitar plato
def deshabilitar_plato(tabla):
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Sin selección", "⚠️ No hay plato seleccionado para deshabilitar.")
        return

    for item in seleccionado:
        valores = list(tabla.item(item, 'values'))
        identificador = valores[0]
        nombre = valores[1]

        confirmar = messagebox.askyesno("Confirmar deshabilitación",
                                        f"¿Deseas deshabilitar el plato '{nombre}'?")
        if confirmar:
            try:
                inactivar_plato(identificador)
                valores[-1] = "No"
                tabla.item(item, values=valores)
                messagebox.showinfo("Plato deshabilitado", f"🟡 El plato '{nombre}' ha sido marcado como inactivo.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Cancelado", f"No se modificó el estado de '{nombre}'.")

# 🧩 Vista principal
def dibujar_pantalla_platos(frame_derecho):
    for widget in frame_derecho.winfo_children():
        widget.destroy()

    estilo = ttk.Style()
    estilo.theme_use("default")
    estilo.configure("Platos.Treeview", font=('Aptos', 14), rowheight=32)
    estilo.configure("Platos.Treeview.Heading", font=('Aptos', 14, 'bold'))

    frame_lista = tk.Frame(frame_derecho, bg='white', bd=2, relief='groove')
    frame_lista.pack(fill='both', expand=True, padx=20, pady=20)

    lbl_titulo = tk.Label(frame_lista, text="Lista de Platos",
                          font=('Aptos', 18, 'bold'), bg='white')
    lbl_titulo.pack(pady=(0, 10))

    frame_tabla = tk.Frame(frame_lista, bg='white')
    frame_tabla.pack(fill='both', expand=True)

    columnas = ("ID", "Nombre", "Descripción", "Precio", "Activo")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show='headings',
                         height=15, style="Platos.Treeview")
    tabla.pack(side='left', fill='both', expand=True)

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor='center')

    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    platos = listar_platos()
    for p in platos:
        tabla.insert("", "end", values=(
            p.identificador,
            p.nombre,
            p.descripcion,
            f"S/ {p.precio:.2f}",
            "Sí" if p.activo else "No"
        ))

    frame_botones = tk.Frame(frame_lista, bg='white')
    frame_botones.pack(fill='x', pady=(10, 0))

    btn_agregar = tk.Button(frame_botones, text="Agregar Plato", font=('Aptos', 12),
                            bg='#27AE60', fg='white', padx=10, pady=5,
                            activebackground='#1E8449', cursor='hand2',
                            command=lambda: agregar_plato_ui(frame_derecho))
    btn_agregar.pack(side='left', padx=10)

    btn_deshabilitar = tk.Button(frame_botones, text="Deshabilitar Plato", font=('Aptos', 12),
                                 bg='#F39C12', fg='white', padx=10, pady=5,
                                 activebackground='#D68910', cursor='hand2',
                                 command=lambda: deshabilitar_plato(tabla))
    btn_deshabilitar.pack(side='left', padx=10)
