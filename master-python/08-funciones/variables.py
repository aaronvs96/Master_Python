"""
Variables locales: se definen dentro de la función y no se puede
usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos un return.

Variables globales: son las que se declaran fuera de una función 
y están disponibles dentro y fuera de ellas.
"""

#Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres."
print(frase)

def holaMundo():
    frase = "Hola Mundo!!"
    print("Dentro de la función:")
    print(frase)

    year=2021
    print(year)

    global website
    website = "victorroblesweb.es"
    print("DENTRO: ",website)

    return "Dato de vuelto " + str(year)


print(holaMundo())
print("FUERA: ",website)