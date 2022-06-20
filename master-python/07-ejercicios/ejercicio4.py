"""
EJERCICIO 4

Pedir dos números al usuario y hacer 
todas las operaciones básicas de una calculadora
"""

num1=int(input("Primer número: "))
num2=int(input("Segundo número: "))

print("-------- SUMA --------")
print("La suma es: " + str(num1+num2)) #ejemplo de concatenacion

print("\n-------- RESTA --------")
print(f"La resta es: {num1-num2}")

print("\n-------- MULTIPLICACION --------")
print(f"La multiplicacion es: {num1*num2}")

print("\n-------- DIVISION --------")
print(f"La division es: {num1/num2}")

print("\n-------- POTENCIA --------")
print(f"La potencia es: {pow(num1,num2)}")

