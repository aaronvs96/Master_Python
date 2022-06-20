"""
Ejercicio 3:
Programa que compruebe si una variable está vacía, y si 
está vacía rellenarla en texto con minúsculas y mostrarlo
en mayúsculas.
"""

dato = input("Ingresar variable: ")

if len(dato.strip())<=0:
    print("VARIABLE VACÍA.")
    dato="Hola mundo"
    minu=dato.lower()
    print(minu.upper())
else:
    print(f"VALOR DE VARIABLE: {dato}")