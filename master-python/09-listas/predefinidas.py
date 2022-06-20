cantantes = ['2pac','Drake','Bad Bunny','Julio Iglesias']
numeros =  [1,2,5,8,3,4]

#Ordenar
print(numeros)
numeros.sort() #metodo sort() sirve para ordenar
print(numeros)

#Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1,"David Bisbal") #dos parametros, indice y valor
print(cantantes)

#Eliminar elementos
cantantes.pop(1)
cantantes.remove('Bad Bunny') #eliminar por el valor
print(cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print('Drake' in cantantes)

#Contar de elementos
print(cantantes)
print(len(cantantes)) #cuenta la cantidad de cantantes en la lista
print(len(cantantes[1])) #cuenta la cantidad de caracteres del indice 1

#Cuantas veces aparece un numero
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
print(cantantes.index('Drake'))

#Unir listas
cantantes.extend(numeros) #une la lista 'numeros' dentro de la lista 'cantantes'
print(cantantes)