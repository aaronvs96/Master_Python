
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}."

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