num = int(input("Ingrese un número entero positivo: "))

es_primo = True
if num < 2:
    es_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

if es_primo and num != 0 and num != 1:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")