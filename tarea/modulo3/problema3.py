
def horas_dormidas_en_una_semana():
    horas_dormidas = 0
    for dia in range(1, 8):
        horas = int(input(f"Ingrese las horas que durmió el día {dia}: "))
        horas_dormidas += horas

    print(f"Durmió un total de {horas_dormidas} horas en la semana.")
    
    if horas_dormidas < 35:
        print("Parece que no has dormido lo suficiente esta semana. Trata de dormir más.")
    elif horas_dormidas >= 35 and horas_dormidas < 49:
        print("Has dormido bien esta semana. ¡Sigue así!")
    else:
        print("Has dormido mucho esta semana. Trata de equilibrar tus horas de sueño para tener un descanso adecuado.")

horas_dormidas_en_una_semana()
