"""
LISTAS(arrays)
Son colecciones o conjunto de datos/valores de dats bajo un unico
nombre.
Para acceder a esos valores podemos usar un índice numérico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman","Spiderman","El Señor de los Anillos"] #definicion normal
cantantes = list(('2pac','Drake','Jennifer Lopez')) #definicion con funcion list, se ingresa como tupla
years=list(range(2020,2050)) #definir con list y range
variada = ["Aaron",30,4.3,True,"cadena"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices
pelicula = "otra cosa"
peliculas[1] = "Gran Torino" #reemplaza el índice 1 del array original
peliculas[2]="El Hobbit"

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:2])
print(cantantes[1:])
print(peliculas[2:])


# Añadir elemento a lista
cantantes.append("Kase O")
cantantes.append("Nator y Waor")
print(cantantes)


#Recorrer lista

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula!="parar":
        peliculas.append(nueva_pelicula)

print("\n*************** Lista de peliculas ******************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

