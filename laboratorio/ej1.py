# Importar el módulo "strerror" del paquete "os".
from os import strerror

# Inicializar un diccionario con 26 contadores para cada letra latina.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# Solicitar al usuario que ingrese el nombre del archivo a analizar y almacenar en la variable "file_name".
file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    file = open(file_name, "rt") # Intentar abrir el archivo en modo lectura de texto ('rt') y asignarlo a la variable "file".
    for line in file:     # Iterar sobre cada línea del archivo.
        for char in line: # Iterar sobre cada carácter en la línea.           
            if char.isalpha():  # Si el carácter es una letra
                counters[char.lower()] += 1 # lo tratamos en minúsculas y actualizamos el contador correspondiente en el diccionario "counters".

    file.close() # Cerrar el archivo después de leerlo.

    # Imprimir la salida de los contadores para cada letra que tenga un recuento mayor que cero.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)

# Capturar una excepción en caso de que ocurra un error de E/S (por ejemplo, el archivo no se encuentra).
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))


