while True:
    try:
        x=int(input('ingrese el diviendo: '))
        y=int(input('ingrese el divisor: '))
        n=x/y
        print('resultado division es: ', n)
        break
    except ZeroDivisionError:
        print('no se puede dividir por cero')
    except ValueError:
        print('valor no aceptado')
    except:
        print('error general')
    