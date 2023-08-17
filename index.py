# importar el flask
from flask import Flask, render_template


app = Flask(__name__)


# definir la ruta
@app.route("/")
@app.route("/index")

# funcion con el saludo
def bienvenida():
    # una variable se define
    return render_template("index.html")


# definir otra ruta
@app.route("/curso")

# funcion con el saludo
def Curso():
    return "curso basico de flask v1"


@app.route("/horario")
def Turno():
    return "Mañana , Tarde y Noche"


@app.route("/sede")
def Sede():
    return "<h1>S.J.L</h1>"


# definir otra ruta
# @app.route('/fichapdf')

# funcion con el saludo
# def fichapdf():
#    return ficha.blade.php
