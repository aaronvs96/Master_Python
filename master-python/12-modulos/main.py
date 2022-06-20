"""
Módulos:
Son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya viene en el lenguaje,
modulos en internet y también podemos crear nuestros módulos
"""
#Importar modulo propio
#import mimodulo
#from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Aaron Vásquez"))
#print(mimodulo.calculadora(10,3,True))

print(holaMundo("Aarón Vásquez"))
print(calculadora(10,3,True))


#Modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.day)
print(fecha_completa.month)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada ",fecha_personalizada)

print(datetime.datetime.now().timestamp())


#Modulo matematicas
import math

print("Raiz cuadrada de 10: ",math.sqrt(10))

print("Numero pi",float(math.pi))

print("Redondear: ",math.ceil(95.3))#redondea al maximo
print("Redondear: ",math.floor(95.3))#redondea al minimo

#Modulo random
import random

print("Numero aleatorio entre 15 y 67: ",random.randint(15,67))#numero aleatorio entre dos numeros
