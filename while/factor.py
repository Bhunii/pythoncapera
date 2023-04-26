a = int(input('numero: '))
b = int(input('numero: '))

while a%b != 0:
    a = int(input('numero: '))
    b = int(input('numero: '))
    if a%b == 0 or b%a == 0:
        print('es factor')
    

