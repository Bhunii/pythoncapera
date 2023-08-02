import os 

def crearArchivo(archivo):
    try:
        with open(archivo, 'x') as file:
            print('Se ha creado el archivo') 
    except FileExistsError:
        print('Ya existe un archivo con este nombre')

def contarLineasArchivo(archivo):
    try:
        with open(archivo, 'rt') as file:
            return len(file.readlines())
    except IOError as e:
        print(f'Se produjo un error: {e}')

def dataArchivo(archivo):
    try:
        with open(archivo, 'wt') as file:
            nombres=input('Digite sus nombres: ')
            apellidos=input('Digite sus apellidos: ')
            nro_identificacion=input('Digite su numero de identificacion: ')
            telefono=input('Digite su numero telefonico: ')
            file.write(f'{nombres} {apellidos}\n{nro_identificacion}\n{telefono}')
    except IOError as e:
        print(f'Sucedio un error:{e}')

def contarCaracteresArchivo(archivo):
    try:
        contador_caracteres=0
        with open(archivo, 'rt') as file:
            linea = file.readline()
            while linea != '':
                for char in linea:
                    contador_caracteres+=1
                linea=file.readline()
        contador_caracteres-=contarLineasArchivo(archivo)
        return contador_caracteres
    except IOError as e:
        print(f'Se produjo un error: {e}')


