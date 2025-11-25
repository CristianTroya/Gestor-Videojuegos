import sqlite3 # Importamos la librería

class DatabaseManager:
    def __init__(self, ):
        
        self.conexion = sqlite3.connect("tareas.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
       self.cursor.execute("""
           CREATE TABLE IF NOT EXISTS Videojuego (
               id INTEGER PRIMARY KEY,
               Nombre TEXT NOT NULL,
               Descripción TEXT NOT NULL,
               Tiempo_estimado INTEGER NOT NULL,
               Tipo TEXT NOT NULL,
               Completado INTEGER NOT NULL,
               Nota_media REAL NOT NULL
           )
       """)
       self.conexion.commit()
       
    def añadir_juego(self, titulo, descripcion, tiempo_estimado, tipo, completado, nota_media):
        self.cursor.execute("INSERT INTO Videojuego (Nombre, Descripción, Tiempo_estimado, Tipo, Completado, Nota_media) VALUES (?, ?, ?, ?, ?, ?)",
                               (titulo, descripcion, tiempo_estimado, tipo, completado, nota_media))
        self.conexion.commit()
  
    def obtener_lista_juegos(self):
       """
       Devuelve la lista de videojuegos en tuplas.\n
       (id, Nombre, Descripción...)[]
       """
       # los obtenemos de la base de datos y se devuelven
       self.cursor.execute("SELECT id, Nombre, Descripción, Tiempo_estimado, Tipo, Completado, Nota_media FROM Videojuego ORDER BY Nombre") # ordenamos por nombre
       return self.cursor.fetchall()
  
    def borrar_juego(self, id):
        self.cursor.execute("DELETE FROM Videojuego WHERE id = ?", (id,))
        self.conexion.commit()