import usuarios.conexion as conexion #importamos la conexion al bd que está en usuarios

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Nota:
    # se crea el constructor, coloco ="" para titulo y descripcion en caso no se guarde nada en esos campos.
    def __init__(self,usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):#metodo guardar
        sql = ("INSERT INTO notas VALUES(null,%s,%s,%s,NOW())")#la funcion NOW reemplaza al atributo fecha
        nota = (self.usuario_id,self.titulo,self.descripcion)#variable nota que guarda los valores de cada atributo

        cursor.execute(sql,nota)#se ejecuta la consulta sql con los datos de la variable nota
        database.commit()#se usa commit para guardar en la base de datos

        return [cursor.rowcount,self]#retorna la fila que se ha guardado
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id={self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount,self]