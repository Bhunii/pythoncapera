cant = int (input('IDigite hasta que numero finaliza: '))
n =  int (input('Digite el numero al que le quiere encontrar multiplo: '))

for k in range(1, cant, 1):
    if k%n == 0:
        print(f'{k} es multiplo de {n}')
    else:
        print(k)