from flask import Flask, flash, redirect, request, url_for, render_template
from datetime import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'clave_secreta_flask'


#Conexion DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

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




#RUTA PARA LLENAR FORMULARIO DE CREAR-COCHE  / RECIBE EL METODO POST DEL FORMULARIO crear_coche.html
@app.route('/crear-coche', methods = ['GET', 'POST']) #SE LE AGREGA LOS METODOS QUE PUEDE RECIBIR DEL FORMULARIO, YA SEA GET O POST
def crear_coche():
    if request.method == 'POST':
        marca = request.form['marca'] #lo que va dentro de los corchetes son los name que están en el formulario html
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
         
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (marca, modelo, precio, ciudad)) #el id es autoincremental por eso se pone NULL
        cursor.connection.commit() #se hace commit para guadar los datos en la base de datos
        
        flash('Haz creado el coche correctamente!!')

        return redirect(url_for('index'))

    return render_template('crear_coche.html')



@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor() # se crea la variable cursor
    cursor.execute('SELECT * FROM coches ORDER BY id DESC') #en la variable cursor se ejecuta la consulta SQL
    coches = cursor.fetchall() #en la variable coches se guarda todos los datos de la tabla coches que estan guardados en cursor
    cursor.close() # se cierra el cursor

    return render_template('coches.html', coches=coches)


@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor() 
    cursor.execute('SELECT * FROM coches WHERE id = %s', (coche_id,)) 
    coche = cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche=coche[0]) #se envia coche[0] porque es el primer elemento en la consulta



@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    cursor = mysql.connection.cursor() 
    cursor.execute(f'DELETE FROM coches WHERE id = {coche_id}') 
    cursor.connection.commit()
    
    flash('El coche ha sido eliminado!!')

    return redirect(url_for('coches'))



@app.route('/editar-coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
         
        cursor = mysql.connection.cursor()
        cursor.execute("""
                        UPDATE coches 
                        SET marca = %s,
                            modelo = %s,
                            precio = %s,
                            ciudad = %s
                        WHERE id =  %s     
                    """, (marca, modelo, precio, ciudad, coche_id)) 
        cursor.connection.commit()
        
        flash('Haz editado el coche correctamente!!')

        return redirect(url_for('coches'))

    cursor = mysql.connection.cursor() 
    cursor.execute('SELECT * FROM coches WHERE id = %s', (coche_id,)) 
    coche = cursor.fetchall()
    cursor.close()

    return render_template('crear_coche.html', coche=coche[0]) #se envia coche[0] porque es el primer elemento en la consulta





#vamos a verificar que el nombre de la aplicación de flask es __main__
if __name__ == '__main__':
    app.run(debug=True)