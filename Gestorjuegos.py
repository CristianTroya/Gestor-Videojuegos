import tkinter as tk

class Videojuego:
 """
 Clase Videojuego, un videojuego dentro del gestor
 """
 def __init__(self, titulo: str, descripcion: str, tiempo_estimado: int, nota_media: float, tipo: str, completado: bool =False):
     """
     Inicializamos una nueva instancia
     - titulo: el título del juego `string`
     - descripción: descripción del juego `string`
     - tiempo_estimado: tiempo estimado para completar el juego `integer`
     - nota_media: nota media del juego sobre 10 `float`
     - tipo: tipo o género del juego `string`
     - completado: ¿Se ha completado el juego? `bool`
     """

     self.id = None
     self.titulo = titulo
     self.descripcion = descripcion
     self.tiempo_estimado = tiempo_estimado
     self.nota_media = nota_media
     self.tipo = tipo
     self.completado = completado

     # Se devolverá en el método del buscador
     self.fila = None

 def __str__(self):
     return f"[{self.id}] {self.titulo}"

ventana = tk.Tk()
ventana.title("Gestor de videojuegos")
ventana.geometry("1280x720")

videojuego1 = Videojuego("SilkGod", "Silkgod mejor juego del año", "30h", "11/10", "tipo")
videojuego2 = Videojuego("Metroid Prime 4", "Descripción de metroid prime 4", "50h", "10/10", "tipo")

videojuegos = [videojuego1, videojuego2]

# Buscador
def buscar(entrada):
 entrada = entrada.lower()
 resultado = -1 # -1 indica que no se ha encontrado nada

 # Comprobamos en cada videojuego si su titulo empieza por la entrada
 for juego in videojuegos:
     if juego.titulo.lower().startswith(entrada):
         resultado = juego.fila
         break

 return resultado

etiqueta_buscador = tk.Entry(ventana, width=50)
etiqueta_buscador.grid(row=0, column=3)
boton_buscador = tk.Button(ventana, text="Buscar")

# Creamos la información para cada videojuego
# usamos el index i para saltar una fila por juego
for indice, v in enumerate(videojuegos):
 indice += 1 # 0 está reservado para el buscador

 etiqueta_titulo = tk.Label(ventana, text=v.titulo)
 etiqueta_desc = tk.Label(ventana, text=v.descripcion)
 etiqueta_tiempo_estimado = tk.Label(ventana, text=v.tiempo_estimado)
 etiqueta_nota = tk.Label(ventana, text=v.nota_media)
 etiqueta_tipo = tk.Label(ventana, text=v.tipo)

 etiqueta_titulo.grid(row=indice, column=0)
 etiqueta_desc.grid(row=indice, column=1)
 etiqueta_tiempo_estimado.grid(row=indice, column=2)
 etiqueta_nota.grid(row=indice, column=3)
 etiqueta_tipo.grid(row=indice, column=4)

 v.fila = indice

def ventana_añadir():
 nueva_ventana = tk.Toplevel(ventana)
 nueva_ventana.title("Añadir videojuego")
 nueva_ventana.geometry("500x300")

 title = tk.Label(nueva_ventana, text="Título del videojuego")
 desc = tk.Label(nueva_ventana, text="Descripción del videojuego")
 estimated_time = tk.Label(nueva_ventana, text="Tiempo estimado para completarlo")
 rate = tk.Label(nueva_ventana, text="Nota media")
 type = tk.Label(nueva_ventana, text="Tipo de videojuego")
 completed = tk.Label(nueva_ventana, text="¿Completado?")

 title.grid(row=0, column=0)
 desc.grid (row=0, column=1)
 estimated_time.grid(row=0, column=2)
 rate.grid(row=2, column=0)
 type.grid(row=2, column=1)
 completed.grid(row=2, column=2)

 title_entry = tk.Entry(nueva_ventana, text="Título del videojuego")
 desc_entry = tk.Entry(nueva_ventana, text="Descripción del videojuego")
 estimated_entry= tk.Entry(nueva_ventana, text="Tiempo estimado para completarlo")
 rate_entry = tk.Entry(nueva_ventana, text="Nota media")
 type_entry = tk.Entry(nueva_ventana, text="Tipo de videojuego")
 completed_entry = tk.Entry(nueva_ventana, text="¿Completado?")
 
 title.grid(row=0, column=0)
 desc.grid (row=0, column=1)
 estimated_time.grid(row=0, column=2)
 rate.grid(row= 2, column=0)
 type.grid(row=2, column=1)
 completed.grid(row=2, column=2)

# Añadir juego
boton_añadir = tk.Button(ventana, text="Añadir juego", command=ventana_añadir)
boton_añadir.grid(row=0, column=4)

ventana.mainloop()
