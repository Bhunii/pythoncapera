x,y=3,5 #se definen variable 'x','y' con valores de 3,5 de manera abreviada 
cont=1 #se define variable 'cont' con un valor dse 1
while not(x%y==0 or y%x==0): #se inicia ciclo indefinido en el que se invierte la expresion en donde el residuo de la division es 0 para saber si son factor
    print(f'intento numero {cont}') #imprime la cantidad de intentos que lleva dentro del print va la variable 'cont' que permite estar hay por 'f'
    x=int(input('ingrese numero')) #'x' pide entrda de dato que es tipó entero
    y=int(input('ingrese numero')) #'y' pide entrda de dato que es tipó entero
    cont+=1 # se crea contador que es igual a la misma varible mas una constante

print(f'{x} y {y} son factor') #si el residuo de la division es 0 imprime las variable 'x' y 'y' que permite estar hay por 'f'