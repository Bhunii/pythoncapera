def LlenarLista(rango):
    for i in range(rango):
        i+=1
        lista.append(i)
    return lista

def Elemento(lista, indice):
    try:
        elemento = lista[indice]
        return res
    except IndexError:
        print("Indice no válido.")
        return None

mi_lista = [10, 20, 30, 40, 50]

lista=LlenarLista(30)
print=lista

resultado1 = obtener_elemento(mi_lista, 2)
print(resultado1)