a = 2
b = 3
c, s = 0, 0
while a<b :
    a = int(input('Ingrese numero: '))
    b = int(input('Ingrese numero: '))
    if a > b:
        c = c + a
        print(f'numero mayor es {c}')
    if b > a:
        s = s + b
        print(f'numero mayor es {s}')
        
