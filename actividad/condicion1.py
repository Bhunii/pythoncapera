a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
c = float(input("Tercero numero: "))

numero = a
if numero > b:
    numero = b
if numero > c:
    numero = c
        
print("El mayor es: ", numero)