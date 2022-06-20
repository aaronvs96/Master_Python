"""
EJERCICIO 5:
Hacer un programa que muestre todos los numeros entre dos
numeros que diga el usuario.
"""

bandera=1

while bandera==1:

    num_i = int(input("Número de la izquierda: "))
    num_d = int(input("Número de la derecha: "))

    if num_i<num_d:

        for contador in range(num_i+1,num_d):

            print(contador)
            contador+=1
            
        bandera=0

    else:

        print("Rango incorrecto.")
        bandera=1