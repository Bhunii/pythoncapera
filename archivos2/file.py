
archivo='archivo/himno.txt'
try:
    contador=1
    stream= open(archivo, 'rt', encoding='utf-8')
    linea = stream.readline()
    while linea != '':           
        print(f'{contador} {linea}')
        linea=stream.readline()
        contador+=1
    stream.close()
except IOError as e:
    print(f'Se produjo un error {e}')

