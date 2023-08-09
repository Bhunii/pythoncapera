import mysql.connector
from funciones import *
from funciones1 import *

base=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_project"
)

cursor=base.cursor()

# insertarDatos(base,cursor)
# mostrarDatos(cursor,'candidato')
eliminarDatos(base,cursor)












# print(type(base))
# cursor.execute("describe candidato")
# print(cursor)
# for data in cursor:
#     print(data)
