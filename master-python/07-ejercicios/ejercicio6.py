"""
EJERCICIO 6:
Tabla de multiplicar del 1 al 10.
Mostrar el título de la tabla y las multiplicaciones.
"""

""""
a x b = ??
a x 1 = ?
a x 2 = ?
a x 3 = ?
a x 4 = ?
a x 5 = ?
a x 6 = ?
a x 7 = ?
a x 8 = ?
a x 9 = ?
a x 10 = ?
"""

a=1 #inicia en la tabla del 1
b=1 #multiplicando

while a<=10:
    print(f"\nTabla del {a}: ")
    for b in range(1,11):        
        print(f"{a} x {b} = {a*b}")
        b+=1
    a+=1