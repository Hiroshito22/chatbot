#importar el flask
from flask import Flask

app = Flask(__name__)
#definir la ruta con una variable(entre llaves {})
@app.route('/operacion/<s>')

#funcion con mostrar datos path
def ResultadoSuma(s):

    return f"<h1>La suma es: {s}</h1>"

#tipos de Datos
#Texto --------> string
#Entero --------> int
#Real --------> float
#------------------------------------------------------------------------
#Definir la ruta con una variable
@app.route('/suma_float/<float:n1>/<float:n2>')

#funcion con mostrar datos path
def CalculaSumaFloat(n1=0,n2=0):
    return f"<h1>La suma es: {n1+n2}</h1>"
#------------------------------------------------------------------------
@app.route('/suma_int/<int:n1>/<int:n2>')
@app.route('/suma_int')
@app.route('/suma_int/<int:n1>')

#funcion con mostrar datos path
def CalculaSumaInt(n1=0,n2=0):
    if n1==None and n2==None:
        return "<h1>No hay numero imbeccil</h1>"
    elif n2==None:
        return f"La suma es {n1}"
    else:
        return f"<h1>La suma es: {n1+n2}</h1>"