# importar el flask
from flask import Flask


app = Flask(__name__)


# definir la ruta
@app.route("/datos")

# funcion con el saludo
def DatosPersonales():
    return "Hiroshi Nizama Garay"
