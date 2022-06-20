"""
SET es un tipo de dato para tener una colección de valores.
No tiene ni índice ni orden.
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")

print(personas) #imprime los elementos en cualquier orden
print(type(personas))