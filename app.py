import tkinter as tk
import sqlite3

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas")
        # ... aquí irá todo el código de la interfaz ...

# --- Código para lanzar la aplicación ---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = App(ventana_principal)
    ventana_principal.mainloop()