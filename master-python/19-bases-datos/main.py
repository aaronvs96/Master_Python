import mysql.connector

# Conexion 
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# La conexion fue correcta?
#print(database)

# Cursor: permite ejecutar las consultas
cursor = database.cursor(buffered=True) #colocar el buffered para hacer varias consultas
# si no colocamos buffered habra error


# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd) #imprime todas las bases de datos
"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""

#cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',18500)")
coches=[
    ('Seat','Ibiza',5000),
    ('Renault','Clio',15000),
    ('Citroen','Saxo',2000),
    ('Mercedes','Clase C',35000)
]
#cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)

database.commit()

#muestra los coches que su precio sea menor igual a 5000 y de la marca Seat
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("----- TODOS MIS COCHES -------")
for coche in result:
    print(coche[1],coche[2],coche[3])

#mostrar solo la primera fila de la tabla
cursor.execute("SELECT * FROM vehiculos")
coche=cursor.fetchone()
print(coche)

#borrar los vehiculos de la marca renault
cursor.execute("DELETE FROM vehiculos WHERE marca='Mercedes'")
database.commit()

#mostrar cantidad de registros borrados
print(cursor.rowcount," registros borrados!!")


#Actualizar
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
database.commit()
print(cursor.rowcount," registros actualizados!!")