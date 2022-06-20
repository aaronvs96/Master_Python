"""
Ejercicio 2:
Escribir un programa que añada valores a una lista mientras
que su longitud sea menor a 120 y luego mostrar la lista.

Plus: USAR WHILE Y FOR (de las dos formas)
"""

lista=[]
tam = 0

tipo_bucle = int(input("¿Qué tipo de bucle se va ejecutar?\n1: While\n2:For\nEscriba número..."))

if tipo_bucle==1:
    while tam<120:
        lista.append(f"elemento-{tam}")
        print("Mostrando el: "+lista[tam])
        tam+=1
    print(lista)
else:
    if tipo_bucle==2:
        for contador in range(120):
            lista.append(f"elemento-{contador}")
            print("Mostrando el: "+lista[contador])

        print(lista)