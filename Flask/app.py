import sqlite3
from flask import Flask, render_template

# Creamos una instancia de la aplicación. __name__ ayuda a Flask a localizar archivos
app = Flask(__name__)

# Definimos una ruta. El símbolo @ es un decorador que vincula la URL con la función de abajo
@app.route("/") # Cuando el usuario entre en la dirección raíz (home)
def inicio():
    conexion = sqlite3.connect("../videojuegos.db")

    # 2. Configuramos la conexión para que devuelva diccionarios (más fácil para Jinja2)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()

    # 3. Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM Videojuego")

    # 4. Guardamos todos los resultados en una variable
    datos = cursor.fetchall()

    # 5. Cerramos la conexión
    conexion.close()

    return render_template("index.html", items=datos)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)
