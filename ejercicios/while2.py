a = 20
b = 21
c, c1 = 0, 0
n = -1
while not(a == b or b == a): 
    a = int(input('Ingrese numero: '))
    b = int(input('Ingrese numero: '))
    if a > b:
        c = c + a
        print(f'numero mayor es {c}')
        while n != 0:
            c1 = a -b
            if a - b > 0:
                print(f'su resta es {c1} ')
while a > n:
    c1 = a - b 

#terminar
    