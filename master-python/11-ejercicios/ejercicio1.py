"""
Una lista de 8 numeros enteros:
- recorrerla y mostrarla
- hacer funcion que recorra listas de numeros y devuelva un string.
- ordenarla y mostrarla
- mostrar longitud
- buscar algun elemento que introduzca el usuario.
"""

lista = [12,3,43,22,1,6,88,67]

print("****** Recorrer y mostrar con función *********")
def mostrarlista(numeros):
    resultado=""

    for numero in numeros:
        resultado+=str(numero)
        resultado+="\n"
    
    return resultado

print(mostrarlista(lista))

print("****** Recorrer y mostrar *********")
for elemento in lista:
    print(elemento)

print("\n****** Ordenar y mostrar *********")
lista.sort()
print(mostrarlista(lista))

print("\n****** Mostrar longitud *********")
print(len(lista))

try:
    print("\n****** Buscar elemento *********")
    busqueda = int(input("Ingrese número a buscar: "))

    comprobar = isinstance(busqueda,int)
    while not comprobar or busqueda<=0:
        busqueda = int(input("Ingrese número a buscar: "))
    else:
        print(f"Haz introducido el {busqueda}")

    print(f"##### Buscar en la lista el numero {busqueda} ######")

    buscar = lista.index(busqueda)
    print(f"El numero buscado existe en la lista, es el índice: {buscar}")
except:
    print("El numero no está en la lista.")