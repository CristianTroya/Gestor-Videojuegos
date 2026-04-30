import tkinter as tk
import json
from tkinter import messagebox
from database_manager import DatabaseManager

class Videojuego:
   """
   Clase Videojuego, un videojuego dentro del gestor
   """
   def __init__(self, titulo, descripcion_corta, descripcion, tiempo_estimado, nota_media, tipo, completado=0, imagen=None):
       """
       Inicializamos una nueva instancia
       - titulo: el título del juego `string`
       - descripcion_corta: descripción corta del juego `string`
       - descripcion: descripción del juego `string`
       - tiempo_estimado: tiempo estimado para completar el juego `integer`
       - nota_media: nota media del juego sobre 10 `float`
       - tipo: tipo o género del juego `string`
       - completado: ¿Se ha completado el juego? `1` o `0`
       """

       self.id = None
       self.titulo = titulo
       self.descripcion_corta = descripcion_corta
       self.descripcion = descripcion
       self.tiempo_estimado = tiempo_estimado
       self.nota_media = nota_media
       self.tipo = tipo
       self.completado = completado
       self.imagen = imagen

   def __str__(self):
       return f"[{self.id}] {self.titulo}"

class App:

   def __init__(self, ventana):
       self.ventana = ventana
       self.ventana.geometry("1300x550")
       self.ventana.title("Gestor de videojuegos")

       self.barra_menu = tk.Menu(self.ventana)
       self.ventana.config(menu=self.barra_menu)

        # Creamos el menú desplegable "Archivo"
       menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
       self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
       menu_archivo.add_separator()
       menu_archivo.add_command(label="Guardar y salir", command=self.ventana.destroy)

       # Creamos el menú desplegable "Ayuda"
       menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
       self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
       menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
       menu_ayuda.add_command(label="¿Cómo usar?", command=self.mostrar_ayuda)

       # convertir a json
       menu_archivo.add_command(label="Exportar a JSON", command=self.exportar_json)
       menu_archivo.add_command(label="Importar desde JSON", command=self.importar_json)


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
        desc_short = tk.Label(frame_añadir, text="Descripción corta del videojuego")
        desc = tk.Label(frame_añadir, text="Descripción del videojuego")
        estimated_time = tk.Label(frame_añadir, text="Tiempo estimado para completarlo")
        rate = tk.Label(frame_añadir, text="Nota media")
        type = tk.Label(frame_añadir, text="Tipo de videojuego")
        image = tk.Label(frame_añadir, text="Imagen")

        # Posicionamos las etiquetas
        title.grid(row=0, column=0)
        desc_short.grid(row=0, column=1)
        desc.grid (row=0, column=2)
        estimated_time.grid(row=0, column=3)
        rate.grid(row= 2, column=0)
        type.grid(row=2, column=1)
        image.grid(row=2, column=2)

        # Campos rellenables
        title_entry = tk.Entry(frame_añadir, text="Título del videojuego")
        desc_entry_short = tk.Entry(frame_añadir, text="Descripción corte del videojuego")
        desc_entry = tk.Entry(frame_añadir, text="Descripción del videojuego")
        estimated_entry= tk.Entry(frame_añadir, text="Tiempo estimado para completarlo")
        rate_entry = tk.Entry(frame_añadir, text="Nota media")
        type_entry = tk.Entry(frame_añadir, text="Tipo de videojuego")
        image_entry = tk.Entry(frame_añadir, text="Imagen")

        # Casilla marcable
        checkbox_var = tk.BooleanVar()
        completed_entry = tk.Checkbutton(frame_añadir, text="¿Completado?", variable=checkbox_var)

        # Posicionamos los campos rellenables y la casilla
        title_entry.grid(row=1, column=0)
        desc_entry_short.grid(row=1, column=1)
        desc_entry.grid (row=1, column=2)
        estimated_entry.grid(row=1, column=3)
        rate_entry.grid(row=3, column=0)
        type_entry.grid(row=3, column=1)
        image_entry.grid(row=3, column=2)
        completed_entry.grid(row=4, column=1)

        # La usaremos para convertir el True/False de la casilla marcable
        # convertir True  -> 1
        #           False -> 0
        def autenticidad(bool):
            if bool==True: return 1
            return 0

        # obtenemos todos los campos
        def al_presionar():
            # Order: titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen
            titulo_val = title_entry.get()
            desc_short_val = desc_entry_short.get()
            desc_val = desc_entry.get()
            estimated_val = estimated_entry.get()
            tipo_val = type_entry.get()
            completado_val = autenticidad(checkbox_var.get())
            nota_val = rate_entry.get()
            imagen_val = image_entry.get()

            self.añadir_juego(
                titulo_val,
                desc_short_val,
                desc_val,
                estimated_val,
                tipo_val,
                completado_val,
                nota_val,
                imagen_val
            )

        # Botón para añadir el juego en la pantalla emergente
        añadir = tk.Button(nueva_ventana, text="Añadir", command=al_presionar)
        añadir.grid(row=4, column=1)

   def ventana_modificar(self, id):
        print("Has presionado modificar (se ha creado una ventana)")

        juego_row = self.db.obtener_juego(id)
        if juego_row is None:
            messagebox.showerror("Error", f"No se encontró el juego con id {id}")
            return

        # Support older DB rows with missing 'Imagen' column (8 fields) or new with 9 fields
        if len(juego_row) == 9:
            _, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen = juego_row
        elif len(juego_row) == 8:
            _, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media = juego_row
            imagen = ''
        else:
            # unexpected shape
            messagebox.showerror("Error", "Registro de juego con formato inesperado")
            return

        # La nueva ventana, encima de la principal
        nueva_ventana = tk.Toplevel(self.ventana)
        nueva_ventana.title("Modificar videojuego")
        nueva_ventana.geometry("700x300")

        frame_añadir = tk.Frame(nueva_ventana)
        frame_añadir.grid(padx=10, pady=10)

        # Etiquetas
        title = tk.Label(frame_añadir, text="Título del videojuego")
        desc_short = tk.Label(frame_añadir, text="Descripción corta del videojuego")
        desc = tk.Label(frame_añadir, text="Descripción del videojuego")
        estimated_time = tk.Label(frame_añadir, text="Tiempo estimado para completarlo")
        rate = tk.Label(frame_añadir, text="Nota media")
        type = tk.Label(frame_añadir, text="Tipo de videojuego")
        image = tk.Label(frame_añadir, text="Imagen")

        # Posicionamos las etiquetas
        title.grid(row=0, column=0)
        desc_short.grid(row=0, column=1)
        desc.grid (row=0, column=2)
        estimated_time.grid(row=0, column=3)
        rate.grid(row= 2, column=0)
        type.grid(row=2, column=1)
        image.grid(row=2, column=2)

        # Campos rellenables
        title_entry = tk.Entry(frame_añadir)
        desc_entry_short = tk.Entry(frame_añadir)
        desc_entry = tk.Entry(frame_añadir)
        estimated_entry= tk.Entry(frame_añadir)
        rate_entry = tk.Entry(frame_añadir)
        type_entry = tk.Entry(frame_añadir)
        image_entry = tk.Entry(frame_añadir)

        # Rellenamos con los datos ya existentes
        title_entry.insert(-1, titulo)
        desc_entry_short.insert(-1, descripcion_corta)
        desc_entry.insert(-1, descripcion)
        estimated_entry.insert(-1, tiempo_estimado)
        rate_entry.insert(-1, nota_media)
        type_entry.insert(-1, tipo)
        image_entry.insert(-1, imagen)

        # Casilla marcable
        checkbox_var = tk.BooleanVar()
        completed_entry = tk.Checkbutton(frame_añadir, text="¿Completado?", variable=checkbox_var)
        # Set checkbox variable according to stored value
        if completado:
            checkbox_var.set(1)

        # Posicionamos los campos rellenables y la casilla
        title_entry.grid(row=1, column=0)
        desc_entry_short.grid(row=1, column=1)
        desc_entry.grid (row=1, column=2)
        estimated_entry.grid(row=1, column=3)
        rate_entry.grid(row=3, column=0)
        type_entry.grid(row=3, column=1)
        image_entry.grid(row=3, column=2)
        completed_entry.grid(row=4, column=2)

        # La usaremos para convertir el True/False de la casilla marcable
        # convertir True  -> 1
        #           False -> 0
        def autenticidad(bool):
            if bool==True: return 1
            return 0

        # obtenemos todos los campos
        def al_presionar():
            # Order: id, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen
            self.modificar_juego(
                id,
                title_entry.get(),
                desc_entry_short.get(),
                desc_entry.get(),
                estimated_entry.get(),
                type_entry.get(),
                autenticidad(checkbox_var.get()),
                rate_entry.get(),
                image_entry.get()
            )

        # Botón para añadir el juego en la pantalla emergente
        añadir = tk.Button(nueva_ventana, text="Modificar", command=al_presionar)
        añadir.grid(row=4, column=1)

   def comprobar_campos_juego(self, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen):
        # Comprobamos que los campos no estén vacíos
        for parametro in [titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, imagen]:
            if str(parametro) == "":
                self.mostrar_error() # Mostramos error si está vacío
                print("Uno o más parámetros están vacíos, no se ha añadido el juego")
                return False
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
            return False
        return True
        
   def modificar_juego(self, id, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen):
        ok = self.comprobar_campos_juego(titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen)
        if not ok:
            return

        # Database expects: id at end
        self.db.modificar_juego(id, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen)
        self.mostrar_juegos()
        print("Has pulsado modificar juego!")

   def añadir_juego(self, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen):
        ok = self.comprobar_campos_juego(titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen)
        if not ok:
            return

        # Order matches DatabaseManager.añadir_juego
        self.db.añadir_juego(titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen)
        self.mostrar_juegos()
        print("Has pulsado añadir juego!")

    # Recorta el texto, lo usamos para la descripción
   def recortar(self, text):
           if text is None:
               return ''
           s = str(text)
           if len(s) >= 30:
               return s[:30] + "..."
           return s

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

       juegos.insert(0, ("id", "Titulo", "Descripción_Corta", "Descripción", "Tiempo estimado", "Tipo", "Completado", "Nota media", "Imagen"))
       for indice, v in enumerate(juegos):
           # Obtenemos los datos de la tupla
           # soportamos filas de 8 o 9 elementos (sin/p con 'Imagen')
           if len(v) == 9:
               id, titulo, desc_short, desc, tiempo_estimado, tipo, completado, nota_media, imagen = v
           elif len(v) == 8:
               id, titulo, desc_short, desc, tiempo_estimado, tipo, completado, nota_media = v
               imagen = ''
           else:
               # saltarse filas con formato inesperado
               continue

           # Etiquetas
           etiqueta_titulo = tk.Label(frame, text=titulo, fg='green' if completado == 1 else None)
           etiqueta_desc_short = tk.Label(frame, text=self.recortar(desc_short), fg='green' if completado == 1 else None)
           etiqueta_desc = tk.Label(frame, text=self.recortar(desc), fg='green' if completado == 1 else None)
           etiqueta_tiempo_estimado = tk.Label(frame, text=tiempo_estimado, fg='green' if completado == 1 else None)
           etiqueta_nota = tk.Label(frame, text=nota_media, fg='green' if completado == 1 else None)
           etiqueta_tipo = tk.Label(frame, text=tipo, fg='green' if completado == 1 else None)
           etiqueta_imagen = tk.Label(frame, text=imagen, fg='green' if completado == 1 else None)

           # usamos lambda para que el índice se acutlice
           # de ahí que la función al_presionar esté fuera del bucle for
           etiqueta_borrar = tk.Button(frame, text="x", command=lambda i=id: self.borrar_juego(i))
           etiqueta_editar = tk.Button(frame, text="🖉", command=lambda i=id: self.ventana_modificar(i))

           # Posicionamos las etiquetas
           etiqueta_titulo.grid(row=indice, column=0, sticky="w")
           etiqueta_desc_short.grid(row=indice, column=1, sticky="w", padx=50)
           etiqueta_desc.grid(row=indice, column=2, sticky="w", padx=50)
           etiqueta_tiempo_estimado.grid(row=indice, column=3, sticky="w", padx=50)
           etiqueta_nota.grid(row=indice, column=4, sticky="w", padx=50)
           etiqueta_tipo.grid(row=indice, column=5, sticky="w", padx=50)
           etiqueta_imagen.grid(row=indice, column=6, sticky="W", padx=50)

           if indice != 0:
            etiqueta_editar.grid(row=indice, column=7, sticky="w", padx=50)
            etiqueta_borrar.grid(row=indice, column=7, sticky="w", padx=10)

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

   def exportar_json(self):
        # 1. Pedimos todos los datos al gestor de la BD
        tareas = self.db.obtener_lista_juegos()

        lista_de_diccionarios = []
        for tarea in tareas:
            # Convertimos cada tupla en un diccionario
            juego = {
                'id': tarea[0],
                'titulo': tarea[1],
                'descripcion_corta': tarea[2],
                'descripcion': tarea[3],
                'tiempo_estimado': tarea[4],
                'tipo': tarea[5],
                'completado': tarea[6],
                'nota_media': tarea[7],
                'imagen': tarea[8]
            }
            lista_de_diccionarios.append(juego)

        # 2. Escribimos la lista de diccionarios en un archivo .json
        try:
            with open('backup_videojuegos.json', 'w', encoding='utf-8') as f:
                json.dump(lista_de_diccionarios, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Exportación Exitosa", "Datos exportados a backup_videojuegos.json")
        except Exception as e: # Capturamos cualquier error que pueda ocurrir
            messagebox.showerror("Error de Exportación", f"No se pudo exportar: {e}")


   def importar_json(self):
        try:
            with open('backup_videojuegos.json', 'r', encoding='utf-8') as f:
                # json.load lee el archivo 'f' y lo convierte a una lista de Python
                lista_de_juegos = json.load(f)

            for tarea in lista_de_juegos:
                # Insertamos cada tarea en la BD usando las claves del diccionario
                self.db.añadir_juego(
                    tarea['titulo'],
                    tarea['descripcion_corta'],
                    tarea['descripcion'],
                    tarea['tiempo_estimado'],
                    tarea['tipo'],
                    tarea['completado'],
                    tarea['nota_media'],
                    tarea['imagen']
                )
                # (Nota: esto no importa el estado 'completada' o el 'id', se podría mejorar)

            self.mostrar_juegos()
            messagebox.showinfo("Importación Exitosa", "Datos importados desde backup_videojuegos.json")

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo 'backup_videojuegos.json'")
        except Exception as e:

            messagebox.showerror("Error de Importación", f"No se pudo importar: {e}")

if __name__ == "__main__":
   ventana_principal = tk.Tk()
   app = App(ventana_principal)
   ventana_principal.mainloop()
