import pandas as pd

file=pd.read_csv('archivosCSV/canciones.csv', header=None)
canciones=file.iloc[:,3]

print(canciones)
