"""
# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


#Operadores de comparación
== igual
!= diferente
< menor
> mayor
<= menor o igual que
>= mayor o igual que

#Operadores Lógicos
and Y
or O
!  negacion
not NO

"""

#Ejemplo1
print("############ EJEMPLO 1 #############")

color = "verde"
#color = input("¿Advivina cuál es mi color favorito?: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("Color incorrecto.")

#Ejemplo2
print("\n############ EJEMPLO 2 #############")

year = 2020
#year = int(input("¿En qué año estamos?: "))

if year>=2021:
    print("Estamos de 2021 en adelante.")
else:
    print("Es un año anterior a 2021.")

#Ejemplo3
print("\n############ EJEMPLO 3 #############")

nombre = "Aaron Vásquez"
ciudad = "Barcelona"
continente = "Oceanía"
edad = 18
mayoria_edad = 18

if edad>=mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente!="Europa":
        print(f"El usuario no es europeo.")
    else:
        print(f"Es europeo y de {ciudad}")

else:
    print(f"{nombre} es mayor de edad.")

#Ejemplo4
print("\n############ EJEMPLO 4 #############")

#dia=int(input("Introduce el día de la semana:"))
dia=3
'''
if dia==1:
    print("Es Lunes")
else:
    if dia==2:
        print("Es martes")
    else:
        if dia==3:
            print("Es miercoles")
        else:
            if dia==4:
                print("Es jueves")
            else:
                if dia==5:
                    print("Es viernes")
'''
if dia==1:
    print("Es lunes")
elif dia==2:
    print("Es martes")
elif dia==3:
    print("Es miercoles")
elif dia==4:
    print("Es jueves")
elif dia==5:
    print("Es viernes")
else:
    print("Es fin de semana")


#Ejemplo5
print("\n############ EJEMPLO 5 #############")

edad_minima=18
edad_maxima=65
edad_oficial=17
#edad_oficial=int(input("¿Tienes edad de trabajar?¿Ingresa tu edad?: "))

if edad_oficial>=18 and edad_oficial<=65:
    print("Está en edad de trabajar !!")
else:
    print("No está en edad de trabajar")


#Ejemplo6
print("\n############ EJEMPLO 6 #############")

pais = "España"

if pais=="Mexico" or pais=="Colombia" or pais=="España":
    print(f"{pais} es un país de habla hispana !!")
else:
    print(f"{pais} no es un país de habla hispana.")

#Ejemplo7
print("\n############ EJEMPLO 7 #############")

pais = "España"

if not(pais=="Mexico" or pais=="Colombia" or pais=="España"):
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SI es un país de habla hispana.")


#Ejemplo8
print("\n############ EJEMPLO 8 #############")

pais = "USA"

if pais!="Mexico" and pais!="España" and pais!="Colombia":
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SI es un país de habla hispana.")