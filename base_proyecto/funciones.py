import mysql.connector

def insertarDatos(nbase, ncursor):
    nro_identificacion=input('digite su numero de documento: ')
    nombre=input('digite sus nombre: ')
    apellidos=input('digite sus apellidos: ')
    correo=input('digite su correo electronico: ')
    telefono=input('digite su numero telefonico: ')
    aux = "INSERT INTO candidato (nro_identificacion, nombre, apellidos, correo_electronico, telefono) VALUES ('"+ nro_identificacion +"','"+ nombre +"','"+ apellidos +"','"+ correo +"','"+ telefono +"')"
    #values = (nro_identificacion, nombre, apellidos, correo, telefono)
    ncursor.execute(aux)
    nbase.commit()

def mostrarDatos(ncursor,tabla):
    query = f"SELECT * FROM {tabla}"
    ncursor.execute(query)
    result = ncursor.fetchall()
    for row in result:
        print(row)

def actualizarDatos(nbase,ncursor):
    nro_identificacion = input("Digite el número de documento del candidato a actualizar: ")
    nuevo_nombre = input("Digite el nuevo nombre: ")
    nuevo_apellido = input("Digite el nuevo apellido: ")
    nuevo_correo = input("Digite el nuevo correo electrónico: ")
    nuevo_telefono = input("Digite el nuevo número telefónico: ")
    query = "UPDATE candidato SET nombre = %s, apellidos = %s, correo_electronico = %s, telefono = %s WHERE nro_identificacion = %s"
    values = (nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_telefono, nro_identificacion)
    ncursor.execute(query, values)
    nbase.commit()
    print("Datos actualizados exitosamente.")

def eliminarDatos(nbase, ncursor):
    nro_identificacion = input("Digite el número de documento del candidato a eliminar: ")
    query = "DELETE FROM candidato WHERE nro_identificacion = %s"
    values = (nro_identificacion,)
    ncursor.execute(query, values)
    nbase.commit()
    print("Datos eliminados exitosamente.")




