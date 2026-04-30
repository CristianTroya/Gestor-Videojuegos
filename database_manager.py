import sqlite3, os # Importamos la librería

class DatabaseManager:
    def __init__(self, ruta):
        db_path = os.path.join(os.path.dirname(__file__), ruta)

        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
       self.cursor.execute("""
           CREATE TABLE IF NOT EXISTS Videojuego (
               id INTEGER PRIMARY KEY,
               Nombre TEXT NOT NULL,
               Descripción_Corta TEXT NOT NULL,
               Descripción TEXT NOT NULL,
               Tiempo_estimado INTEGER NOT NULL,
               Tipo TEXT NOT NULL,
               Completado INTEGER NOT NULL,
               Nota_media REAL NOT NULL,
               Imagen TEXT NOT NULL
           )
       """)
       self.conexion.commit()

    def añadir_juego(self, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen):
        self.cursor.execute("INSERT INTO Videojuego (Nombre, Descripción_Corta, Descripción, Tiempo_estimado, Tipo, Completado, Nota_media, Imagen) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen))
        self.conexion.commit()

    def modificar_juego(self, id, titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen):
        self.cursor.execute("UPDATE Videojuego SET Nombre = ?, Descripción_Corta=?, Descripción = ?, Tiempo_estimado = ?, Tipo = ?, Completado = ?, Nota_media = ?, Imagen = ? WHERE id = ?",
                               (titulo, descripcion_corta, descripcion, tiempo_estimado, tipo, completado, nota_media, imagen, id))
        self.conexion.commit()

    def obtener_lista_juegos(self):
       """
       Devuelve la lista de videojuegos en tuplas.\n
       (id, Nombre, Descripción...)[]
       """
       # los obtenemos de la base de datos y se devuelven
       self.cursor.execute("SELECT * FROM Videojuego ORDER BY Nombre") # ordenamos por nombre
       return self.cursor.fetchall()

    def obtener_juego(self, id):
        """
        Devuelve las propiedades de un videojuego
        """
        self.cursor.execute("SELECT id, Nombre, Descripción_Corta, Descripción, Tiempo_estimado, Tipo, Completado, Nota_media, Imagen FROM Videojuego WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def borrar_juego(self, id):
        self.cursor.execute("DELETE FROM Videojuego WHERE id = ?", (id,))
        self.conexion.commit()
