from modules.reportes import *

# Menú principal
def main():
    while True:
        print("\n" + "="*70)
        print("SISTEMA DE REPORTES - RESTAURANTE")
        print("="*70)
        print("1. Reporte por Fecha")
        print("2. Reporte por Plato")
        print("3. Reporte por Mesero")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            ReporteporFecha()
        elif opcion == "2":
            ReporteporPlato()
        elif opcion == "3":
            ReporteporMesero()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()