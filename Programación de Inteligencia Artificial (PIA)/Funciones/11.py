def tiempo_a_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

print(tiempo_a_segundos(1, 30, 10))  # 5410