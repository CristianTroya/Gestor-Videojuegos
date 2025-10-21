import tkinter as tk

class Videojuego:
    """
    Clase Videojuego, un videojuego dentro del gestor
    """
    def __init__(self, titulo, descripcion, tiempo_estimado, nota_media, tipo, completado=False):
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

videojuego1 = Videojuego("SilkGod", "Descripción Silkgod", "30h", "11/10", "metroidvania souls")
videojuego2 = Videojuego("Metroid Prime 4", "Descripción de metroid prime 4", "50h", "10/10", "metroidvania")
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

frame_buscador = tk.Frame(ventana)
frame_buscador.grid()

etiqueta_buscador = tk.Entry(frame_buscador, width=50)
etiqueta_buscador.grid(row=0, column=1 )
boton_buscador = tk.Button(frame_buscador, text="Buscar")

def borrar_juego(indice):
    videojuegos.pop(indice - 1)

def mostrar_juegos(juegos):
    # Creamos la información para cada videojuego

    # Creamos el frame
    frame_juegos = tk.Frame(ventana)
    frame_juegos.grid()

    for indice, v in enumerate(juegos):
        indice += 1 # 0 está reservado para el buscador

        etiqueta_titulo = tk.Label(ventana, text=v.titulo)
        etiqueta_desc = tk.Label(ventana, text=v.descripcion)
        etiqueta_tiempo_estimado = tk.Label(ventana, text=v.tiempo_estimado)
        etiqueta_nota = tk.Label(ventana, text=v.nota_media)
        etiqueta_tipo = tk.Label(ventana, text=v.tipo)

        def al_presionar():
            borrar_juego(indice)
            mostrar_juegos(videojuegos)
            print("Has pulsado borrar")

        etiqueta_borrar = tk.Button(ventana, text="x", command=al_presionar)

        etiqueta_titulo.grid(row=indice, column=0, sticky="w")
        etiqueta_desc.grid(row=indice, column=1, sticky="w")
        etiqueta_tiempo_estimado.grid(row=indice, column=3, sticky="w")
        etiqueta_nota.grid(row=indice, column=4, sticky="w")
        etiqueta_tipo.grid(row=indice, column=5, sticky="w")
        etiqueta_borrar.grid(row=indice, column=6, sticky="w")

    v.fila = indice

mostrar_juegos(videojuegos)

def añadir_juego(titulo: str, descripcion: str, tiempo_estimado: int, nota_media: float, tipo: str, completado: bool =False):
    juego = Videojuego(titulo, descripcion, tiempo_estimado, nota_media, tipo, completado)
    videojuegos.append(juego)

    mostrar_juegos(videojuegos)

def ventana_añadir():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Añadir videojuego")
    nueva_ventana.geometry("700x300")

    title = tk.Label(nueva_ventana, text="Título del videojuego")
    desc = tk.Label(nueva_ventana, text="Descripción del videojuego")
    estimated_time = tk.Label(nueva_ventana, text="Tiempo estimado para completarlo")
    rate = tk.Label(nueva_ventana, text="Nota media")
    type = tk.Label(nueva_ventana, text="Tipo de videojuego")

    title.grid(row=0, column=0)
    desc.grid (row=0, column=1)
    estimated_time.grid(row=0, column=2)
    rate.grid(row= 2, column=0)
    type.grid(row=2, column=1)

    title_entry = tk.Entry(nueva_ventana, text="Título del videojuego")
    desc_entry = tk.Entry(nueva_ventana, text="Descripción del videojuego")
    estimated_entry= tk.Entry(nueva_ventana, text="Tiempo estimado para completarlo")
    rate_entry = tk.Entry(nueva_ventana, text="Nota media")
    type_entry = tk.Entry(nueva_ventana, text="Tipo de videojuego")

    checkbox_var = tk.BooleanVar()
    completed_entry = tk.Checkbutton(nueva_ventana, text="¿Completado?", variable=checkbox_var)

    title_entry.grid(row=1, column=0)
    desc_entry.grid (row=1, column=1)
    estimated_entry.grid(row=1, column=2)
    rate_entry.grid(row=3, column=0)
    type_entry.grid(row=3, column=1)
    completed_entry.grid(row=3, column=2)
    
    def al_presionar():
        añadir_juego(
        title_entry.get(), 
        desc_entry.get(), 
        estimated_entry.get(), 
        rate_entry.get(), 
        type_entry.get(), 
        checkbox_var.get())

    añadir = tk.Button(nueva_ventana, text="Añadir", command=al_presionar)
    añadir.grid(row=4, column=1)

# Añadir juego
boton_añadir = tk.Button(ventana, text="Añadir juego", command=ventana_añadir)
boton_añadir.grid(row=0, column=4)

ventana.mainloop()