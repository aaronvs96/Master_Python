"""EJERCICIO 5:
Crear una lista con el contenido de esta tabla:
ACCCION     AVENTURA                DEPORTES    
GTA         ASSANSINS               FIFA 21
COD         CRASH                   PRO 21
PUGB        Prince of Persia        MOTO GP 21


MOSTRAR ESTA INFORMACION ORDENADA.
"""

from typing import Counter


nueva_tabla = [
    {
        "categoria":"ACCION",
        "juegos":["AC1","AC2","AC3"]
    },
    {
        "categoria":"DEPORTES",
        "juegos":["DEP1","DEP2","DEP3"]
    }
]

for categoria in nueva_tabla:
    print(f"-----{categoria['categoria']}----")
    for juego in categoria['juegos']:
        print(juego)