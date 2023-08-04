n = int(input('ingrese numero: '))
primo = 0
no_primo = 0

for i in range(2, n):
        if n % i == 0:
            no_primo = no_primo + n
            print(f"{no_primo} no es número primo.")
            break
        if n and n != 0 and n != 1:
             primo = primo + n
             print(f"{primo} es un número primo.")
             break