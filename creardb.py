import sqlite3 # Importamos la librería

# --- PASO 1: Conectar a la base de datos ---
# Se crea el archivo 'tareas.db' si no existe
conexion = sqlite3.connect('videojuego.db')

# Para poder enviar comandos, necesitamos un "cursor"
cursor = conexion.cursor()

# --- PASO 2: Ejecutar un comando SQL ---
# Usamos un string multilínea con triples comillas para que el SQL sea más legible
comando_sql = """
CREATE TABLE IF NOT EXISTS Videojuego (
    id INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Descripción TEXT NOT NULL,
    Tiempo_estimado INTEGER NOT NULL,
    Tipo TEXT NOT NULL,
    Completado INTEGER NOT NULL,
    Nota_media REAL NOT NULL
)
"""
# 'IF NOT EXISTS' evita que nos dé un error si la tabla ya ha sido creada
cursor.execute(comando_sql)

# Para que los cambios se guarden de forma permanente, hacemos un "commit"
conexion.commit()

# --- PASO 3: Cerrar la conexión ---
conexion.close()

print("Tabla 'Videojuego' creada con éxito (si no existía ya).")