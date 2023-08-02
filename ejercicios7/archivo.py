import os 

def archivoExiste(archivo):
    return os.path.exists(archivo)

def crearArchivo(archivo):
    if archivoExiste(archivo):
        print('Ya existe un archivo con este nombre')
    else:
        try:
            stream = open(archivo, 'w')
            print('Se ha creado el archivo')
            stream.close()
        except Exception as e:
            print(f'Error al crear el archivo: {e}')

def contarLineasAarchivo(archivo):
    try:
        contador_lineas=0
        stream= open(archivo, 'rt')
        linea = stream.readline()
        while linea != '':
            contador_lineas += 1
            linea = stream.readline()
        stream.close()
        print(f'Líneas en el archivo: {contador_lineas}')
    except IOError as e:
        print(f'Se produjo un error {e}')

def dataArchivo(archivo):
    try:
        stream = open(archivo, 'wt')
        nombres=str(input('Digite sus nombres: '))
        stream.write(nombres+ ' ')
        apellidos=str(input('Digite sus apellidos: '))
        stream.write(apellidos+ '\n')
        nro_identificacion=int(input('Digite su numero de identificacion: '))
        stream.write(str(nro_identificacion) + '\n')
        telefono=int(input('Digite su numero telefonico: '))
        stream.write(str(telefono)+ '\n')        
        stream.close()
    except IOError as e:
        print(f'Se produjo un error: {e}')


aux='text.txt'
crearArchivo(aux)
contarLineasAarchivo(aux)
dataArchivo(aux)
contarLineasAarchivo(aux)