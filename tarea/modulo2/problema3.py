n = int(input("Ingrese el primer número entero: ")) #se difine variable tipo entero con entrada de dato
m = int(input("Ingrese el segundo número entero: ")) #se difine variable tipo entero con entrada de dato

cociente = n // m #se usa division entera para no tener decimales
resto = n % m #Se usa mod para mostrar el residuo de de la division

print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}") #se imprime respuesta