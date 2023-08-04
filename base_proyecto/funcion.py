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



