"""
EJERCICIO 4:
Crear 4 variables: una lista, un string, un entero y una booleana.
Imprimir el tipo de variable que es cada una.
"""

def comprobarTipo(dato,tipo):
    test = isinstance(dato,tipo)
    result = ""
    if test:
        result = f"Este dato es del tipo {type(dato)}"
    else:
        result=None
    
    return result

var1 = [1,2,"hola",12.5]
var2 = "Hola Mundo"
var3 = 10
var4 = True

print(comprobarTipo(var2,str))
