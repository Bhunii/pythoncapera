import os 

def crearArchivo(archivo):
    try:
        with open(archivo, 'x') as f:
            print('Se ha creado el archivo') 
    except FileExistsError:
        print('Ya existe un archivo con este nombre')

def dataArchivo(archivo):
    nombres=str(input('Digite sus nombres: '))
    apelidos=str(input('Digite sus apellidos: '))
    nro_identificacion=int(input('Digite su numero de identificacion: '))
    telefono=int(input('Digite su numero telefonico: '))
    file.open(archivo, 'wt')
    file.write()

aux=crearArchivo('text.txt')