a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))

if a > b:
        mayor = a
        menor = b
else:
        mayor = b
        menor = a

res = mayor - menor
while res >= menor:
    res = res - menor
        
print(f'El sobrante es: {res}')
    