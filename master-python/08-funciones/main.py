"""
FUNCIONES
Una función es un conjunto de instrucciones agrupadas bajo un
nombre que pueden reutilizarse invocando a la función tantas veces
como sea necesario. 

def nombreDeMiFuncion(parametros):
    # bloque  / conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)

"""


#Ejemplo 1

print("########## EJEMPLO 1 ############")
#Definir funcion
def muestraNombres():
    print("Aarón")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

#Invocar función
"""muestraNombres()
muestraNombres()
muestraNombres()
"""
#Ejemplo 2: parámetros
print("########## EJEMPLO 2 ############")

def mostrarTunombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")
    if edad>=18:
        print("Y eres mayor de edad")

#nombre = input("Introduce tu nombre: ")
#edad=int(input("Ingrese edad: "))
"""mostrarTunombre(nombre,edad)
"""

#Ejemplo 3
print("########## EJEMPLO 3 ############")

def tabla(numero):
    print(f"Tabla de multiplicar del {numero}")

    for contador in range(11):
        operacion=numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)

#Ejemplo 3.1
print("-------------------")
for numero_tabla in range(1,11):
    tabla(numero_tabla)


#Ejemplo 4
print("########## EJEMPLO 4 ############")

#Parámetros opcionales
def getEmpleado(nombre,dni=None):
    print("EMPLEADO")
    print(F"Nombre: {nombre}")
    if dni!=None:
        print(f"DNI: {dni}")

getEmpleado("Aarón Vásquez",71397844)

#Ejemplo 5
# parámetros opcionales y return o devolver datos
print("########## EJEMPLO 5 ############")

def saludame(nombre):
    saludo=f"Hola, saludos {nombre}"
    return saludo

print(saludame("Aarón"))

#Ejemplo 6
print("########## EJEMPLO 6 ############")

def calculadora(num1,num2, basicas=False):
    suma = num1 + num2
    resta = num1 - num2
    producto = num1*num2
    division = num1/num2

    cadena="" 

    if basicas!=False:
        cadena+= "Suma: " +str(suma)
        cadena +=  "\n"
        cadena += "Resta: " + str(resta)
        cadena+="\n"
    else:
        cadena+= "Suma: " +str(suma)
        cadena +=  "\n"
        cadena += "Resta: " + str(resta)
        cadena+="\n"
        cadena+="Multiplicación: " + str(producto)
        cadena+="\n"
        cadena +="División: " + str(division)

    return cadena

print(calculadora(2,4,True))


#Ejemplo7
print("############# EJEMPLO 7 ##############")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"\nLos apellidos son: {apellidos}"
    return texto

def devuelteTodo(nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelteTodo("Aarón", "Vásquez"))

#Ejemplo8: funcion lambda
print("\n############# EJEMPLO 8 ##############")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))



