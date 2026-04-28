import sqlite3, os
from flask import Flask, render_template

# Creamos una instancia de la aplicación. __name__ ayuda a Flask a localizar archivos
app = Flask(__name__)

# Ubicación del archivo database
db_path = os.path.join(os.path.dirname(__file__), "../videojuegos.db")


# Definimos una ruta. El símbolo @ es un decorador que vincula la URL con la función de abajo
@app.route("/") # Cuando el usuario entre en la dirección raíz (home)
def inicio():
    conexion = sqlite3.connect(db_path)

    # 2. Configuramos la conexión para que devuelva diccionarios (más fácil para Jinja2)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # 3. Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM Videojuego")

    # 4. Guardamos todos los resultados en una variable
    datos = cursor.fetchall()

    # 5. Cerramos la conexión
    conexion.close()

    for item in datos:
        print(item["Nombre"], item["Descripción"], item["Imagen"])

    return render_template("index.html", items=datos)

@app.route("/detalle/<int:id_item>")
def ver_detalle(id_item):
    # 1. Abrimos conexión con la base de datos
    conexion = sqlite3.connect(db_path)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    # 2. Buscamos el elemento que tenga exactamente ese ID
    # El símbolo ? evita ataques de Inyección SQL
    cursor.execute("SELECT * FROM Videojuego WHERE id = ?", (id_item,))
    
    # 3. fetchone() obtiene solo UN resultado (el que coincide con el ID)
    item_encontrado = cursor.fetchone()
    conexion.close()
    
    # 4. Enviamos los datos del elemento a una plantilla específica
    return render_template("detalle.html", item=item_encontrado)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)
