
def horas_dormidas_en_una_semana(): #se define una funcion 
    horas_dormidas = 0 #se define variable y se asigna su valor
    for dia in range(1, 8): #se inicia ciclo for que tendra un rango de 1 a 8 
        horas = int(input(f"Ingrese las horas que durmió el día {dia}: ")) #se define variable tipo entero con entrada de texto y se usa f para mostrar a {dia} la variable del ciclo
        horas_dormidas += horas #'horas_dormidas' es una variable que es igual a la misma varible mas una constante(en este caso 'horas')

    print(f"Durmió un total de {horas_dormidas} horas en la semana.") #cantidad total de horas dormidas en las 7 veces que se repitio for
    
    if horas_dormidas < 35: #se evalua que si 'horas_dormidas' es menor a '35' siga a:
        print("Parece que no has dormido lo suficiente esta semana. Trata de dormir más.") #salida de texto con mensaje relacionado
    elif horas_dormidas >= 35 and horas_dormidas < 49: #elif evalua una segunda opcion en que 'horas_dormidas' debe estar entre un rango de 35 a 48 para segui a:
        print("Has dormido bien esta semana. ¡Sigue así!") #salida de texto con mensaje relacionado
    else: #en cada que ninguna de las dos pasa a:
        print("Has dormido mucho esta semana. Trata de equilibrar tus horas de sueño para tener un descanso adecuado.") #salida de texto con mensaje relacionado

horas_dormidas_en_una_semana() #se cierra la funcion
