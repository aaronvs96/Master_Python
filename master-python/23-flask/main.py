from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

# Context processors
@app.context_processor
def date_now(): #funcion que devuelve la fecha actual al layout
    return {
        'now': datetime.utcnow()
    }


#las rutas se declaran con app.route y una funcion
@app.route('/')#ruta de inicio
def index():

    edad = 101
    personas = ['Victor','Paco','Francisco', 'David']

    return render_template('index.html',
                            edad=edad,
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno","dos","tres"],
                            personas=personas
                        )



@app.route('/informacion') #esta es la ruta opcional sin parametro 'nombre'
@app.route('/informacion/<string:nombre>')#podemos definir el tipo de dato
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre = None, apellidos = None): #se le agrega el None al nombre y apellidos cuando no se ingrese el parametro
    
    texto=""
    if nombre!=None and apellidos!=None: #validando si le paso el parametro o no
        texto = f"Bienvenido, {nombre} {apellidos}"
        
    return render_template('informacion.html',
                            texto=texto
                        )


@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):

    if redireccion is not None:
        return redirect(url_for('lenguajes')) #se importa redirect y url_for para redirigir a otra url

    return render_template('contacto.html')



@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')



#vamos a verificar que el nombre de la aplicación de flask es __main__
if __name__ == '__main__':
    app.run(debug=True)