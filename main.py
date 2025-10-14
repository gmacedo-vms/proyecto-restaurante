# main.py
import tkinter as tk
from views.vista_principal import dibujar_pantalla_principal

def main():
    root = tk.Tk()
    dibujar_pantalla_principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()
