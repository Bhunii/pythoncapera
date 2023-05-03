max = 0
num = 1

while num > 0:
    num = int(input("Introduce un número positivo (o negativo para terminar): "))
    if num > max:
        max = num

print(f'El numero maximo es: {max}')