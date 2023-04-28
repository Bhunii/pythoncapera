m = int(input('Ingrese hasta donde finaliza '))
n = int(input('Ingrese numero'))

for j in range(1,m,1):
    if j%n == 0:
        print(f'{j}es divisor de {n}')
    else:
        print(j)