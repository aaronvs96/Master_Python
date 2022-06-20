"""
#FOR
for variable in elemento_iterable  (lista,rango,etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0
for contador in range(0,10):
    print("Voy por el "+str(contador))
    
    resultado += contador

print(f"El resultado es: {resultado}")


#Ejemplo con tablas de multiplicar
print("\n############### EJMEPLO ###############")

numero_usuario = int(input("De qué numero quieres la tabla: "))

if numero_usuario<1:
    numero_usuario=1

print(f"Tabla de multiplicar del numero {numero_usuario} ####")

contador=0
for contador in range(1,13):

    if numero_usuario==45:
        print("No se pueden mostrar números prohibidos")
        break
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
else:
    print("Tabla Finaliza.")