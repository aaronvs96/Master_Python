"""
EJERCICIO 10:
El programa tiene que pedir la nota de 15 alumnos.
sacar en pantalla cuantos han aprobado y
cuantos han suspendido.
"""

contador=1
aprobado=0
suspendido=0
for i in range(1,16):
    nota = int(input(f"Ingresar nota {contador}: "))
    contador+=1
    if nota>=11:
        aprobado+=1
    else:
        suspendido+=1

print(f"Aprobados: ",aprobado)
print(f"Suspendidos: ",suspendido)