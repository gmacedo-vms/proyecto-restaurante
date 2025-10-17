import tkinter as tk
import tkinter.ttk as ttk
import re

from tkinter.ttk import Combobox
from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from modules.usuarios import agregar_usuario as guardar_en_csv


from modules.usuarios import listar_usuarios, inactivar_usuario

# 🟢 Acción: Agregar usuario
def agregar_usuario():
    ventana = Toplevel()
    ventana.title("Agregar Usuario")
    ventana.configure(bg='white')

    # 📐 Tamaño base + 20% vertical y centrado
    ancho = 400
    alto = int(400 * 1.2)  # 480px
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # 🧩 Campos del formulario
    campos = {
        "DNI": StringVar(),
        "Nombre": StringVar(),
        "Apellidos": StringVar(),
        "Usuario": StringVar(),
        "Clave": StringVar(),
        "Correo": StringVar(),
        "Rol": StringVar(value="Mesero")
    }

    for idx, (label, var) in enumerate(campos.items()):
        Label(ventana, text=label, bg='white', font=('Aptos', 12)).pack(pady=(10 if idx == 0 else 5, 0))
        if label == "Rol":
            combo_rol = Combobox(ventana, textvariable=var, font=('Aptos', 12), state="readonly")
            combo_rol['values'] = ["Administrador", "Mesero"]
            combo_rol.current(1)
            combo_rol.pack()
        elif label == "Clave":
            Entry(ventana, textvariable=var, font=('Aptos', 12), show="*").pack()
        else:
            Entry(ventana, textvariable=var, font=('Aptos', 12)).pack()

    def confirmar():
        rol_seleccionado = campos["Rol"].get()
        rol = "admin" if rol_seleccionado == "Administrador" else "mesero"
        rol_descripcion = rol_seleccionado

        dni_valor = campos["DNI"].get()
        if not re.fullmatch(r"\d{8}", dni_valor):
            messagebox.showwarning("DNI inválido", "El DNI debe contener exactamente 8 dígitos numéricos.")
            return

        datos = {
            'identificador': dni_valor,
            'nombre': campos["Nombre"].get(),
            'apellidos': campos["Apellidos"].get(),
            'usuario': campos["Usuario"].get(),
            'clave': campos["Clave"].get(),
            'correo': campos["Correo"].get(),
            'rol': rol,
            'rol_descripcion': rol_descripcion,
            'activo': "true"
        }

        if not all([datos[k] for k in datos if k != 'activo']):
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        try:
            guardar_en_csv(datos)
            messagebox.showinfo("Usuario agregado", f"✅ Usuario '{datos['usuario']}' guardado correctamente.")
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(ventana, text="Guardar", font=('Aptos', 12), bg='#27AE60', fg='white',
           padx=10, pady=5, command=confirmar).pack(pady=20)


# 🟡 Acción: Inactivar usuario
def inactiva_usuario(tabla):
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Sin selección", "⚠️ No hay usuario seleccionado para inactivar.")
        return

    for item in seleccionado:
        valores = list(tabla.item(item, 'values'))
        usuario = valores[2]  # Asumiendo que el campo 'Usuario' está en la tercera posición

        # Confirmación antes de inactivar
        confirmar = messagebox.askyesno("Confirmar inactivación",
                                        f"¿Deseas inactivar al usuario '{usuario}'?")
        if confirmar:
            inactivar_usuario(usuario)  # 🔁 Actualiza el CSV
            valores[-1] = "No"  # Actualiza visualmente en la tabla
            tabla.item(item, values=valores)
            messagebox.showinfo("Usuario inactivado", f"🟡 El usuario '{usuario}' ha sido marcado como inactivo.")
        else:
            messagebox.showinfo("Cancelado", f"No se modificó el estado de '{usuario}'.")


# 🧩 Vista principal
def dibujar_pantalla_usuarios(frame_derecho):
    # 🧹 Limpiar contenido previo
    for widget in frame_derecho.winfo_children():
        widget.destroy()

    # 🎨 Estilos personalizados
    estilo = ttk.Style()
    estilo.theme_use("default")
    estilo.configure("Usuarios.Treeview", font=('Aptos', 14), rowheight=32)
    estilo.configure("Usuarios.Treeview.Heading", font=('Aptos', 14, 'bold'))

    # 🧩 Contenedor principal
    frame_lista = tk.Frame(frame_derecho, bg='white', bd=2, relief='groove')
    frame_lista.pack(fill='both', expand=True, padx=20, pady=20)

    # 🏷️ Título
    lbl_titulo = tk.Label(frame_lista, text="Lista de Usuarios",
                          font=('Aptos', 18, 'bold'), bg='white')
    lbl_titulo.pack(pady=(0, 10))

    # 📦 Subframe exclusivo para tabla + scrollbar
    frame_tabla = tk.Frame(frame_lista, bg='white')
    frame_tabla.pack(fill='both', expand=True)

    columnas = ("DNI", "Nombre", "Usuario", "Correo", "Rol", "Activo")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show='headings',
                         height=15, style="Usuarios.Treeview")
    tabla.pack(side='left', fill='both', expand=True)

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor='center')

    # 🧭 Scroll vertical solo para la tabla
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # 📦 Cargar datos desde listar_usuarios()
    usuarios = listar_usuarios()
    for u in usuarios:
        if all([u.identificador, u.nombre, u.apellidos, u.usuario]):
            tabla.insert("", "end", values=(
                u.identificador,
                f"{u.nombre} {u.apellidos}",
                u.usuario,
                u.correo,
                u.rol_descripcion,
                "Sí" if u.activo else "No"
            ))

    # 🧮 Botones debajo de la tabla
    frame_botones = tk.Frame(frame_lista, bg='white')
    frame_botones.pack(fill='x', pady=(10, 0))

    btn_agregar = tk.Button(frame_botones, text="Agregar Usuario", font=('Aptos', 12),
                            bg='#27AE60', fg='white', padx=10, pady=5,
                            activebackground='#1E8449', cursor='hand2',
                            command=agregar_usuario)
    btn_agregar.pack(side='left', padx=10)

    btn_inactivar = tk.Button(frame_botones, text="Inactivar Usuario", font=('Aptos', 12),
                              bg='#F39C12', fg='white', padx=10, pady=5,
                              activebackground='#D68910', cursor='hand2',
                              command=lambda: inactiva_usuario(tabla))
    btn_inactivar.pack(side='left', padx=10)
