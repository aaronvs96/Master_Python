nombre = "Aaron Vasquez"

# Funciones generales
print(nombre)
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre,str)
if comprobar:
    print("Esa variable es un string.")
else:
    print("No es una cadena.")

if not isinstance(nombre,float):
    print("La variable no es un número con decimales.")

# Limpiar espacios
frase="     mi contenido     "
print(frase)
print(frase.strip()) #frase.strip() -> limpia los espacios

# Eliminar variables
year=2022
print(year)
del year # del-> elimina la variable
#print(year) # imprime un error porque la variable ya no existe

# Comprobar variable vacia
texto = " ff "

if len(texto)>=0:
    print("La variable no está vacía.",len(texto))
else:
    print("La variable está vacía.",len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida")) #devuelve la posicion en la que empieza la palabra

# Reemplazar palabras en un string
nueva_frase=frase.replace("vida","moto") #reemplaza un valor por otro
print(nueva_frase)

# Mayusculas y minúsculas
print(nombre)
print(nombre.lower())
print(nombre.upper())