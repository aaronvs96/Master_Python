"""
EJERCICIO 8:
¿Cuánto es el x por ciento de de x numero?
"""

numero=int(input("Ingresar numero: "))
porcentaje=int(input(f"Porcentaje a sacar de {numero}: "))

if porcentaje<0 or porcentaje>=100:
    print(f"No se puede extraer el {porcentaje} %")
else:
    operacion = (numero * (porcentaje/100))
    print(f"El {porcentaje}% de {numero} es {operacion}")