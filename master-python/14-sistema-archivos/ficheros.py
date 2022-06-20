from io import open
import pathlib
import shutil

#Abrir archivo
ruta = str(pathlib.Path().absolute())+"/fichero_texto.txt" #pathlib ayuda a definir la ruta absoluta
archivo = open(ruta, "a+") #el permiso a+ es para abrir archivo

#Escribir
archivo.write("**********Soy un texto metido desde Python**********\n")

#Cerrar archivo
archivo.close()



#Abrir archivo
ruta = str(pathlib.Path().absolute())+"/fichero_texto.txt" #pathlib ayuda a definir la ruta absoluta
archivo_lectura = open(ruta, "r") #el permiso r que es para lectura de archivos

#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)


#Copiar
"""
ruta_original = str(pathlib.Path().absolute())+"/fichero_texto.txt" #pathlib ayud a definir la ruta absoluta
ruta_nueva = str(pathlib.Path().absolute())+"/fichero_copiado.txt" #pathlib ayud a definir la ruta absoluta
ruta_alternativa = str(pathlib.Path().absolute())+"/../07-ejercicios/fichero_copiado88.txt"

shutil.copyfile(ruta_original,ruta_alternativa)
"""

#Mover: mueve el archivo a otra ruta
#en este ejemplo ya habia un archivo llamado "fichero_copiado"
#lo que se hizo fue moverlo a la misma ruta y cambiarle el nombre
#lo que hizo el programa fue sobreponer el archivo con otro nombre
"""
ruta_original = str(pathlib.Path().absolute())+"/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""

#Eliminar
import os
"""
ruta_nueva = str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"

os.remove(ruta_nueva)
"""

#Comprobar si existe
import os.path

#print(os.path.abspath("../")) #imprime la ruta
ruta_comprobar=os.path.abspath("./")+"/fichero_texto.txt"
#print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe.")
else:
    print("El archivo no existe.")