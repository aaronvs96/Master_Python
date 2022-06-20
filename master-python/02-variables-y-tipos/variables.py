"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden cerar 
muchas variables y que cada una tenga un dato
distinto
"""


#Crear variables y asignarles un valor
texto = "Master en Python"
print(texto)

numero=10
print(numero)
print(type(numero))

decimal=0.2
print(type(decimal))

print("##########")

#Sustituir el valor de algunas variables / reasignando valores
numero=77
print(numero)

print("-------------------------------")

#Concatenación
nombre="Aaron"
apellidos="Vasquez"
web="aaronvasquezweb.es"

print(nombre+" "+apellidos+" - "+web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es {}".format(nombre,apellidos,web))

print(nombre,apellidos,web)
