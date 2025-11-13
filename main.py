import tkinter as tk
import sqlite3

class Videojuego:
    """
    Clase Videojuego, un videojuego dentro del gestor
    """
    def __init__(self, titulo, descripcion, tiempo_estimado, nota_media, tipo, completado=0):
        """
        Inicializamos una nueva instancia
        - titulo: el título del juego `string`
        - descripción: descripción del juego `string`
        - tiempo_estimado: tiempo estimado para completar el juego `integer`
        - nota_media: nota media del juego sobre 10 `float`
        - tipo: tipo o género del juego `string`
        - completado: ¿Se ha completado el juego? `1` o `0`
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

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("900x550")
        self.ventana.title("Gestor de videojuegos")

        videojuego1 = Videojuego("SilkGod", "Descripción Silkgod", "30h", "11/10", "metroidvania souls", 1)
        videojuego2 = Videojuego("Metroid Prime 4", "Descripción de metroid prime 4", "50h", "10/10", "metroidvania")
        videojuegos = [videojuego1, videojuego2]

        frame_juegos = tk.Frame(self.ventana)

        frame_nav = tk.Frame(self.ventana)
        frame_nav.grid(pady=10)

        etiqueta_buscador = tk.Entry(frame_nav, width=50)
        etiqueta_buscador.grid(row=0, column=0, padx=10)

        # Buscador
        def buscar(lista_videojuegos):
            entrada = etiqueta_buscador.get().lower()
            coincidencias = []

            # Comprobamos en cada videojuego si su titulo empieza por la entrada
            for juego in lista_videojuegos:
                if entrada in juego.titulo.lower():
                    coincidencias.append(juego)

            mostrar_juegos(coincidencias, frame_juegos)

        boton_buscador = tk.Button(frame_nav, text="Buscar", command=lambda lista=videojuegos: buscar(lista))
        boton_buscador.grid(row=0, column=1)

        def borrar_juego(indice):
            videojuegos.pop(indice)

        # colocamos el buscador después de la barra de navegación
        frame_juegos.grid(padx=10, pady=10, sticky="w")
        
        def recortar (text):
            if len(text) >= 30:
                return text[:30] + "..."
            return text
        
        def mostrar_juegos(juegos, frame):
            # limpiamos los elementos al actualizarlos
            for elemento in frame.winfo_children():
                elemento.destroy()

            def al_presionar(indice):
                borrar_juego(indice)
                mostrar_juegos(videojuegos, frame_juegos)
                print("Has pulsado borrar!")

            for indice, v in enumerate(juegos):
                etiqueta_titulo = tk.Label(frame, text=v.titulo, fg='green' if v.completado == 1 else None)
                etiqueta_desc = tk.Label(frame, text=v.descripcion, fg='green' if v.completado == 1 else None)
                etiqueta_tiempo_estimado = tk.Label(frame, text=v.tiempo_estimado, fg='green' if v.completado == 1 else None)
                etiqueta_nota = tk.Label(frame, text=v.nota_media, fg='green' if v.completado == 1 else None)
                etiqueta_tipo = tk.Label(frame, text=v.tipo, fg='green' if v.completado == 1 else None)

                # usamos lambda para que el índice se acutlice
                # de ahí que la función al_presionar esté fuera del bucle for
                etiqueta_borrar = tk.Button(frame, text="x", command=lambda i=indice: al_presionar(i))

                etiqueta_titulo.grid(row=indice, column=0, sticky="w")
                etiqueta_desc.grid(row=indice, column=1, sticky="w", padx=10)
                etiqueta_tiempo_estimado.grid(row=indice, column=3, sticky="w", padx=10)
                etiqueta_nota.grid(row=indice, column=4, sticky="w", padx=10)
                etiqueta_tipo.grid(row=indice, column=5, sticky="w", padx=10)
                etiqueta_borrar.grid(row=indice, column=6, sticky="w", padx=10)

                v.fila = indice

        mostrar_juegos(videojuegos, frame_juegos)


        def añadir_juego(titulo, descripcion, tiempo_estimado, nota_media, tipo, completado=1):
            for parametro in [titulo, descripcion, tiempo_estimado, nota_media, tipo]:
                if str(parametro) == "":
                    print("Uno o más parámetros están vacíos, no se ha añadido el juego")
                    return

            try:
                int(tiempo_estimado)
                int(completado)
                float(nota_media)

            except ValueError:
                print("Alguno de los campos numéricos no lo son:")
                print("Tiempo estimado: int, completado: int, nota: real")
                return

            juego = Videojuego(titulo, descripcion, tiempo_estimado, nota_media, tipo, completado)
            videojuegos.append(juego)

            mostrar_juegos(videojuegos, frame_juegos)
            print("Has pulsado añadir juego!")

        def ventana_añadir():
            print("Has presionado añadir (se ha creado una ventana)")
            
            nueva_ventana = tk.Toplevel(self.ventana)
            nueva_ventana.title("Añadir videojuego")
            nueva_ventana.geometry("700x300")
        
            frame_añadir = tk.Frame(nueva_ventana)
            frame_añadir.grid(padx=10, pady=10)

            title = tk.Label(frame_añadir, text="Título del videojuego")
            desc = tk.Label(frame_añadir, text="Descripción del videojuego")
            estimated_time = tk.Label(frame_añadir, text="Tiempo estimado para completarlo")
            rate = tk.Label(frame_añadir, text="Nota media")
            type = tk.Label(frame_añadir, text="Tipo de videojuego")

            title.grid(row=0, column=0)
            desc.grid (row=0, column=1)
            estimated_time.grid(row=0, column=2)
            rate.grid(row= 2, column=0)
            type.grid(row=2, column=1)

            title_entry = tk.Entry(frame_añadir, text="Título del videojuego")
            desc_entry = tk.Entry(frame_añadir, text="Descripción del videojuego")
            estimated_entry= tk.Entry(frame_añadir, text="Tiempo estimado para completarlo")
            rate_entry = tk.Entry(frame_añadir, text="Nota media")
            type_entry = tk.Entry(frame_añadir, text="Tipo de videojuego")

            checkbox_var = tk.BooleanVar()
            completed_entry = tk.Checkbutton(frame_añadir, text="¿Completado?", variable=checkbox_var)

            title_entry.grid(row=1, column=0)
            desc_entry.grid (row=1, column=1)
            estimated_entry.grid(row=1, column=2)
            rate_entry.grid(row=3, column=0)
            type_entry.grid(row=3, column=1)
            completed_entry.grid(row=3, column=2)

            def autenticidad(bool):
                if bool==True: return 1
                return 0
            def al_presionar():
                añadir_juego(
                title_entry.get(), 
                desc_entry.get(), 
                estimated_entry.get(), 
                rate_entry.get(), 
                type_entry.get(), 
                autenticidad(checkbox_var.get()))

            añadir = tk.Button(nueva_ventana, text="Añadir", command=al_presionar)
            añadir.grid(row=4, column=1)

        # Añadir juego
        frame_nav.columnconfigure(2, minsize=370)
        boton_añadir = tk.Button(frame_nav, text="Añadir juego", command=ventana_añadir)
        boton_añadir.grid(row=0, column=2, sticky="e")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = App(ventana_principal)
    ventana_principal.mainloop()