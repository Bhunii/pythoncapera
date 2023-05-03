n = int(input("Digite un numero: "))
sum = 0
div = 1

while sum < n:
    if n % div == 0:
        sum = sum + div
    div = div + 1

if sum == n:
    print(f'{n} es perfecto')
else:
    print(f'{n} no es perfecto')
