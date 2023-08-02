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

def contarLineasArchivo(archivo):
    try:
        contador_lineas=0
        stream= open(archivo, 'rt')
        linea = stream.readline()
        while linea != '':
            contador_lineas += 1
            linea = stream.readline()
        stream.close()
        return contador_lineas
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
        stream.write(str(telefono))        
        stream.close()
    except IOError as e:
        print(f'Se produjo un error: {e}')

def contarCaracteresArchivo(archivo):
    try:
        contador_caracteres=0
        strean = open(archivo, 'rt')
        linea = strean.readline()
        while linea != '':
            for char in linea:
                contador_caracteres+=1
            linea=strean.readline()
        strean.close()
        contador_caracteres-=contarLineasArchivo(archivo)
        return contador_caracteres
    except IOError as e:
        print(f'Se produjo un error: {e}')

