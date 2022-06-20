## Listas multidimensionales
print("\n********** Listado de contactos *********")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

print(contactos[0]) #imprime nombre con su correo 
print(contactos[0][0]) #imprime solo el nombre
print(contactos[0][1]) #imprime solo el correo

print("\n************** USANDO FOR *************")

for contacto in contactos:
    for elemento in contacto:
        if(contacto.index(elemento)==0):
            print("Nombre: "+elemento)
        else:
            print("Email: "+elemento)
    print("\n")