def segundos_a_tiempo(segundos_totales):
    horas = segundos_totales // 3600  # Calculamos las horas
    minutos = (segundos_totales % 3600) // 60  # Calculamos los minutos
    segundos = segundos_totales % 60  # Los segundos restantes
    return horas, minutos, segundos

print(segundos_a_tiempo(3665))  # Salida: (1, 1, 5), porque 3665 segundos es 1 hora, 1 minuto y 5 segundos
print(segundos_a_tiempo(7322))  # Salida: (2, 2, 2), porque 7322 segundos es 2 horas, 2 minutos y 2 segundos
