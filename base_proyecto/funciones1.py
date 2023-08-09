import mysql.connector

def modifTabla(nbase, ncursor, nombretabla):
    columna = input("Nombre de la columna: ")
    tipo = input("Que tipo de dato va a ser?: ")
    
    print("Que quiere hacer?: ")
    print("1-Agregar una columna")
    print("2-Modificar una columna")
    print("3-Eliminar una columna")
    op = int(input())
    
    try:
        if op == 1:
            consulta = f"ALTER TABLE {nombretabla} ADD {columna} {tipo}"
            print("Se ha agregado la nueva columna")
        elif op == 2:
            consulta = f"ALTER TABLE {nombretabla} MODIFY {columna} {tipo}"
            print("Se modifico con exito")
        elif op == 3:
            consulta = f"ALTER TABLE {nombretabla} DROP COLUMN {columna}"
            print("Se elimino la columna")
        else:
            print("Opción no válida")
            return
        
        ncursor.execute(consulta)
        nbase.commit()
        print("Operación exitosa")
    except Exception as e:
        print("Error:", str(e))
    finally:
        ncursor.close()
        nbase.close()


def descriptabla(ncursor):
    nombretabla = input("De qué tabla quieres su descripción?: ")
    aux = f"DESCRIBE {nombretabla}"
    ncursor.execute(aux)
    
    for column_info in ncursor:
        print(column_info)