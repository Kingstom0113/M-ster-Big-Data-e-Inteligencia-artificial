cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

i = 0
son_iguales = True

while i < len(cadena1) and i < len(cadena2):
    if cadena1[i] != cadena2[i]:
        son_iguales = False
        break
    i += 1

if son_iguales and len(cadena1) == len(cadena2):
    print("Las cadenas son iguales.")
else:
    print("Las cadenas son diferentes.")
