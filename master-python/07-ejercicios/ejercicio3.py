"""
EJERCICIO 3
Escribir un programa que muestre los cuadrados de los 60 primeros
numeros naturales.

 - resolverlo con bucle for y bucle while
"""

print("############ CON BUCLE FOR ############")
a=1
for contador in range(1,61):
    print(f"{a} x {a} = {contador*contador}")
    a+=1


print("########## CON BUCLE WHILE ############")

conta=b=1
while conta<61:
    print(f"{b} x {b} = {conta*conta}")
    conta+=1
    b+=1