import tkinter as tk
from tkinter import messagebox
from database_manager import DatabaseManager

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

   def __str__(self):
    return f"[{self.id}] {self.titulo}"

class App:

   def __init__(self, ventana):
       self.ventana = ventana
       self.ventana.geometry("900x550")
       self.ventana.title("Gestor de videojuegos")

       self.barra_menu = tk.Menu(self.ventana)
       self.ventana.config(menu=self.barra_menu)

        # Creamos el menú desplegable "Archivo"
       menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
       self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
       menu_archivo.add_separator()
       menu_archivo.add_command(label="Salir", command=self.ventana.destroy)

       # Creamos el menú desplegable "Ayuda"
       menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
       self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
       menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
       menu_ayuda.add_command(label="¿Cómo usar?", command=self.mostrar_ayuda)
       
       self.db = DatabaseManager("videojuegos.db")

       frame_nav = tk.Frame(self.ventana)
       frame_nav.grid(pady=10)

       self.etiqueta_buscador = tk.Entry(frame_nav, width=50)
       self.etiqueta_buscador.grid(row=0, column=0, padx=10)

       boton_buscador = tk.Button(frame_nav, text="Buscar", command=self.buscar)
       boton_buscador.grid(row=0, column=1)

       self.frame_juegos = tk.Frame(self.ventana)
       self.frame_juegos.grid(padx=10, pady=10, sticky="w")

       # colocamos el buscador después de la barra de navegación
       self.mostrar_juegos()

       # Botón para añadir el juego en la pantalla principal
       frame_nav.columnconfigure(2, minsize=370)
       boton_añadir = tk.Button(frame_nav, text="Añadir juego", command=self.ventana_añadir)
       boton_añadir.grid(row=0, column=2, sticky="e")
   
   def mostrar_acerca_de(self):
        # Toplevel crea una nueva ventana "hija" de la ventana principal
        ventana_acerca_de = tk.Toplevel(self.ventana)
        ventana_acerca_de.title("Acerca de nosotros")
        ventana_acerca_de.geometry("425x200")

        # Hacemos que la ventana sea "modal": bloquea la ventana principal
        ventana_acerca_de.grab_set()
        ventana_acerca_de.transient(self.ventana)

        tk.Label(ventana_acerca_de, text="Gestor de videojuegos").pack(pady=20)
        tk.Label(ventana_acerca_de, text="Desarrolado por: Carlos Rincón, Elio Delgado y Cristian Troya").pack(pady=5)
                
        boton_cerrar = tk.Button(ventana_acerca_de, text="Cerrar", command=ventana_acerca_de.destroy)
        boton_cerrar.pack(pady=20)

   def mostrar_ayuda(self):
        # Toplevel crea una nueva ventana "hija" de la ventana principal
        ventana_ayuda = tk.Toplevel(self.ventana)
        ventana_ayuda.title("¿Cómo usar?")
        ventana_ayuda.geometry("425x200")

        # Hacemos que la ventana sea "modal": bloquea la ventana principal
        ventana_ayuda.grab_set()
        ventana_ayuda.transient(self.ventana)

        tk.Label(ventana_ayuda, text="¿Cómo usar?").pack(pady=20)
        tk.Label(ventana_ayuda, text="El botón añadir juego abre una ventana en la cual\ndebes añadir los datos del videojuego\n\n Al completar la ventana pulsar el botón añadir\npara añadir el videojuego a la tabla\n\n Una vez en la tabla puedes consultar los juegos con\nel buscador o eliminarlos de la tabla con la cruz").pack(pady=0)
        
        boton_cerrar = tk.Button(ventana_ayuda, text="Cerrar", command=ventana_ayuda.destroy)
        boton_cerrar.pack(pady=20)


   def mostrar_error(self):
       # Toplevel crea una nueva ventana "hija" de la ventana principal
       ventana_acerca_de = tk.Toplevel(self.ventana)
       ventana_acerca_de.title("ERROR")
       ventana_acerca_de.geometry("400x250")

       # Hacemos que la ventana sea "modal": bloquea la ventana principal
       ventana_acerca_de.grab_set()
       ventana_acerca_de.transient(self.ventana)

       tk.Label(ventana_acerca_de, text="Ha ocurrido un error al añadir el juego").pack(pady=20)
       tk.Label(ventana_acerca_de, text="Comprueba si has rellenado todas las casillas\n y si el tiempo estimado y la nota media son números").pack(pady=5)
      
       boton_cerrar = tk.Button(ventana_acerca_de, text="Cerrar", command=ventana_acerca_de.destroy)
       boton_cerrar.pack(pady=20)

   def ventana_añadir(self):
        print("Has presionado añadir (se ha creado una ventana)")
        
        # La nueva ventana, encima de la principal
        nueva_ventana = tk.Toplevel(self.ventana)
        nueva_ventana.title("Añadir videojuego")
        nueva_ventana.geometry("700x300")
    
        frame_añadir = tk.Frame(nueva_ventana)
        frame_añadir.grid(padx=10, pady=10)

        # Etiquetas
        title = tk.Label(frame_añadir, text="Título del videojuego")
        desc = tk.Label(frame_añadir, text="Descripción del videojuego")
        estimated_time = tk.Label(frame_añadir, text="Tiempo estimado para completarlo")
        rate = tk.Label(frame_añadir, text="Nota media")
        type = tk.Label(frame_añadir, text="Tipo de videojuego")

        # Posicionamos las etiquetas
        title.grid(row=0, column=0)
        desc.grid (row=0, column=1)
        estimated_time.grid(row=0, column=2)
        rate.grid(row= 2, column=0)
        type.grid(row=2, column=1)

        # Campos rellenables
        title_entry = tk.Entry(frame_añadir, text="Título del videojuego")
        desc_entry = tk.Entry(frame_añadir, text="Descripción del videojuego")
        estimated_entry= tk.Entry(frame_añadir, text="Tiempo estimado para completarlo")
        rate_entry = tk.Entry(frame_añadir, text="Nota media")
        type_entry = tk.Entry(frame_añadir, text="Tipo de videojuego")

        # Casilla marcable
        checkbox_var = tk.BooleanVar()
        completed_entry = tk.Checkbutton(frame_añadir, text="¿Completado?", variable=checkbox_var)

        # Posicionamos los campos rellenables y la casilla
        title_entry.grid(row=1, column=0)
        desc_entry.grid (row=1, column=1)
        estimated_entry.grid(row=1, column=2)
        rate_entry.grid(row=3, column=0)
        type_entry.grid(row=3, column=1)
        completed_entry.grid(row=3, column=2)

        # La usaremos para convertir el True/False de la casilla marcable
        # convertir True  -> 1
        #           False -> 0
        def autenticidad(bool):
            if bool==True: return 1
            return 0
        
        # obtenemos todos los campos
        def al_presionar():
            self.añadir_juego(
            title_entry.get(),
            desc_entry.get(),
            estimated_entry.get(),
            rate_entry.get(),
            type_entry.get(),
            autenticidad(checkbox_var.get())) # Convertimos la variable de la casilla

        # Botón para añadir el juego en la pantalla emergente
        añadir = tk.Button(nueva_ventana, text="Añadir", command=al_presionar)
        añadir.grid(row=4, column=1)

   def añadir_juego(self, titulo, descripcion, tiempo_estimado, nota_media, tipo, completado=1):
        # Comprobamos que los campos no estén vacíos
        for parametro in [titulo, descripcion, tiempo_estimado, nota_media, tipo]:
            if str(parametro) == "":
                self.mostrar_error() # Mostramos error si está vacío
                print("Uno o más parámetros están vacíos, no se ha añadido el juego")
                return
        # si intentamos convertir un texto a número nos devolverá un error
        try:
            int(tiempo_estimado)
            int(completado)
            float(nota_media)

        # si hay error entonces hay texto en un campo de número
        except ValueError:
            self.mostrar_error()
            print("Alguno de los campos numéricos no lo son:")
            print("Tiempo estimado: int, completado: int, nota: real")
            return

        self.db.añadir_juego(titulo, descripcion, tiempo_estimado, tipo, completado, nota_media)
        self.mostrar_juegos()
        print("Has pulsado añadir juego!")

    # Recorta el texto, lo usamos para la descripción
   def recortar(self, text):
       if len(text) >= 30:
           return text[:30] + "..."
       return text

   def mostrar_juegos(self, juegos=[]):
       # siempre usamos el mismo frame declarado en __init__
       frame = self.frame_juegos

       # limpiamos los elementos al actualizarlos
       for elemento in frame.winfo_children():
           elemento.destroy()

       # Si juegos != [], entonces sí se usó el buscador

       # el buscador no devolvió coincidencias
       if juegos == None:
           return
       
       # no se usó el buscador, por tanto mostramos todos los juegos
       if len(juegos) == 0:
        juegos = self.db.obtener_lista_juegos()
       
       for indice, v in enumerate(juegos):
           # Obtenemos los datos de la tupla
           id, titulo, desc, tiempo_estimado, tipo, completado, nota_media = v

           # Etiquetas
           etiqueta_titulo = tk.Label(frame, text=titulo, fg='green' if completado == 1 else None)
           etiqueta_desc = tk.Label(frame, text=self.recortar(desc), fg='green' if completado == 1 else None)
           etiqueta_tiempo_estimado = tk.Label(frame, text=tiempo_estimado, fg='green' if completado == 1 else None)
           etiqueta_nota = tk.Label(frame, text=nota_media, fg='green' if completado == 1 else None)
           etiqueta_tipo = tk.Label(frame, text=tipo, fg='green' if completado == 1 else None)

           # usamos lambda para que el índice se acutlice
           # de ahí que la función al_presionar esté fuera del bucle for
           etiqueta_borrar = tk.Button(frame, text="x", command=lambda i=id: self.borrar_juego(i))
           
           # Posicionamos las etiquetas
           etiqueta_titulo.grid(row=indice, column=0, sticky="w")
           etiqueta_desc.grid(row=indice, column=1, sticky="w", padx=10)
           etiqueta_tiempo_estimado.grid(row=indice, column=3, sticky="w", padx=10)
           etiqueta_nota.grid(row=indice, column=4, sticky="w", padx=10)
           etiqueta_tipo.grid(row=indice, column=5, sticky="w", padx=10)
           etiqueta_borrar.grid(row=indice, column=6, sticky="w", padx=10)

   def borrar_juego(self, id):
        print("Has pulsado borrar!")

        if messagebox.askyesno("Confirmar borrado", "¿Estás seguro?"):
            self.db.borrar_juego(id)
            self.mostrar_juegos()

   def buscar(self):
        # la entrada del buscador
        entrada = self.etiqueta_buscador.get().lower()
        lista_juegos = self.db.obtener_lista_juegos()
        coincidencias = []

        # Comprobamos en cada videojuego si su titulo empieza por la entrada
        for juego in lista_juegos:
            titulo = juego[1].lower() # titulo

            if entrada in titulo:
                coincidencias.append(juego)

        if len(coincidencias) > 0:
            self.mostrar_juegos(coincidencias)
            return
        
        # Le pasamos None para no mostrar juegos
        self.mostrar_juegos(None)

if __name__ == "__main__":
   ventana_principal = tk.Tk()
   app = App(ventana_principal)
   ventana_principal.mainloop()