#un programa que diga cuantas letras tiene cada linea del coro del himno de soacha
#escriba la respuesta en otro archivo
c=0
lista=[]
letras = open('archivos2/coro.txt', 'r', encoding='utf-8')
for linea in letras.readlines():
        for char in linea:
                c+=1
        lista.append(c)  
        print(c)
        c=0
letras.close()

print(lista)

aux=''
conteo = open('archivos2/resultado.txt', 'a', encoding='utf-8')
for i in lista:
    conteo.write(i)
    i+1
conteo.close()
