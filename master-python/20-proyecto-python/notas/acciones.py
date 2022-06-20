import notas.nota as modelo #se importa el modelo nota y le ponemos nombre "modelo"

class Acciones:

    def crear(self,usuario):#metodo crear
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota...")

        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        #se crear variable nota que llama al modelo y la clase Nota
        #la clase Nota tiene 3 atributos
        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()
        
        if guardar[0]>=1:#comprobar si es que se ha guardado bien
            print(f"\nPerfecto haz guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")
    
    def mostrar(self,usuario):
        print(f"Vale {usuario[1]}!! Aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print(f"\nNota: {nota[0]}")
            print(f"Título: {nota[2]}")
            print(f"Contenido: {nota[3]}")
    
    def borrar(sqlf,usuario):
        print(f"\nOkey {usuario[1]}!! Vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0],titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("No se ha borrado la nota, prueba luego...")