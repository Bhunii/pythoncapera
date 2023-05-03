n = int(input("Introduce la altura del triángulo (entero positivo): ")) # se define variable tipo entero con entrada de texto
for i in range(n): #se inicia ciclo for que se ejecutara cantidad de veces segun n
    for j in range(i+1): #se inicia otro cilo for en donde i sera igual a i mas 1 (cada vez aumenta)
        print("*", end="") #'*' para hacer la piramide y end para mantenerlos en la misma linea 
    print("") #para empezar una nueva linea de '*'