from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

num_count = 0
special_count = 0
unknown_count = 0

file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra...
            if char.isalpha():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1
            # Si es un dígito numérico...
            elif char.isdigit():
                num_count += 1
            # Si es un carácter especial.
            else:
                special_count += 1
    file.close()

    # Salida a los contadores de letras.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)

    # Salida a los contadores de caracteres numéricos y especiales.
    print("Caracteres numéricos ->", num_count)
    print("Caracteres especiales ->", special_count)

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
