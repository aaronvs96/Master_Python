"""
EJERCICIO 9:
Hacer un programa que pida numero al usuario indefinidamente
hasta meter el numero 111.
"""

bandera=1
while bandera==1:
    numero = int(input("Ingresar número: "))
    if numero!=111:
        print(f"El numero es: {numero}")
    else:
        bandera=0
        print(f"Haz ingresado {numero}. Se cierra el programa.")