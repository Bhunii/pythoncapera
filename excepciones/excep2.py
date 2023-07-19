import math
def cuadratica(a, b, c, signo):    
    temp=math.sqrt((b**2) - 4 * a * c)
    if signo == '-':
        temp2=(-(b)-temp)/(2*(a))
    if signo == '+':
        temp2=(-(b)+temp)/(2*(a))
    return temp2

def cuadraticaTryExcept(a, b, c, signo):    
    try:
        temp=math.sqrt((b**2) - 4 * a * c)
        if signo == '-':
            temp2=(-(b)-temp)/(2*(a))
        if signo == '+':
            temp2=(-(b)+temp)/(2*(a))
        return temp2        
    except ValueError:
        return 'Valor no acepatable'
    except ZeroDivisionError:
        return 'No se puede dividir por cero'
    except:
        return 'Error inesperado'

aux=cuadratica(5,6,1,'-')
print(aux)
aux2=cuadraticaTryExcept(5,6,1,'-')
print(aux2)

