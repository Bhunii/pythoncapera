# Convertir unidades
# El return "guarda" el resultado, el None para los valores no validos 
# y f permite poner variables

def convertir_unidades(numero, unidad_original, unidad_deseada):
    if unidad_original == "cm" and unidad_deseada == "m":
        return numero / 100
    elif unidad_original == "cm" and unidad_deseada == "km":
        return numero / 100000
    elif unidad_original == "m" and unidad_deseada == "cm":
        return numero * 100
    elif unidad_original == "m" and unidad_deseada == "km":
        return numero / 1000
    elif unidad_original == "km" and unidad_deseada == "cm":
        return numero * 100000
    elif unidad_original == "km" and unidad_deseada == "m":
        return numero * 1000
    else:
        return None

numero = float(input("Ingrese la numero: "))
unidad_original = input("Ingrese la unidad original (cm, m o km): ")
unidad_deseada = input("Ingrese la unidad deseada (cm, m o km): ")

resultado = convertir_unidades(numero, unidad_original, unidad_deseada)

if resultado is None:
    print("No se puede realizar la conversión.")
else:
    print(f"{numero} {unidad_original} son {resultado} {unidad_deseada}.")
