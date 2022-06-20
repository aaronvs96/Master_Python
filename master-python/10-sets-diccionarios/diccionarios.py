"""
Diccionario es un tipo de dato que almacena un conjunto de datos,
en formato clave > valor.

Es parecido a un array asociativo o un objeto json
"""

persona = {
    "nombre":"Aarón",
    "apellido":"Vásquez",
    "web":"aaron@web.com"
}

#print(persona["apellido"])

# Lista de diccionarios

contactos = [
    {
        'nombre':'Antonio',
        'email':'antonio@antonio.com'
    },
    {
        'nombre':'Luis',
        'email':'luis@luis.com'
    },
    {
        'nombre':'Salvador',
        'email':'salvador@salvador.com'
    }
]

contactos[0]['nombre']='Antoñito'
print(contactos[0]['nombre'])

print("\nLista de Contactos: \n")

for contacto in contactos:
    print(f"Nombre de contacto: {contacto['nombre']}")
    print(f"Email de contacto: {contacto['email']}")
    print("-------------------------------------------")