"""
EJERCICIO 7:
Hacer un programa que muestre todos los números impares entre 
dos números que eliga el usuario.
"""

num1=int(input("Primer numero: "))
num2=int(input("Segundo número: "))

if num1<num2:
    for contador in range(num1,num2+1):
        if contador%2!=0:
            print(f"{contador} es impar")
        contador+=1
else:
    print("El primer número debe ser menor.")