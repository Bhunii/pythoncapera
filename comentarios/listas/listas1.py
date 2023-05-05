#[], {}, (), {()}
x=100
print(type(x))
x='Soacha'
print(type(x))
lista=['python',100,[1,2,3,[]],'a'] 
print(type(lista)) #hay un tipo de dato especial para las listas y es 'list'
print(len(lista)) #lee el tamaño de la lista
print(lista[0]) #llamar a un solo dato de la lista, empiezan en cero a 'n' aqui es 0 es 'python'
print(lista[1]) 
print(lista[3])
print(lista[-4]) #tambien se puede contar de 'n' a el primer valor esto se hace de forma negativa siendo el ultimo valor '-1' y el primero '-n' (el primer dato es 'a')
del lista[-2] #'del' es eliminar y en aqui se elimina la sublista
print(lista) 

"""
cuenta1=cuenta() 
cuenta2=cuenta()
cuenta3=cuenta()

cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""