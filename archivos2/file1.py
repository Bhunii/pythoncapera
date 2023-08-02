import os

try:
    stream=open('archivo2/himno.txt', 'r',encoding='utf-8')
    for linea in stream.readlines():
        print(linea)
    stream.close()
except IOError as e:
    print(e)