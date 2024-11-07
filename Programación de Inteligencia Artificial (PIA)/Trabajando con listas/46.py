# Crea una lista de nombres y usa filter() para obtener solo los nombres que comienzan con una vocal.

nombres = ['Ana', 'Elsa', 'Olaf', 'Kristoff', 'Sven', 'Hans', 'Oaken', 'Pabbie', 'Bulda', 'Cliff']

def comienza_con_vocal(nombre):
    vocales = 'aeiou'
    return nombre[0].lower() in vocales

nombres_con_vocal = filter(comienza_con_vocal, nombres)
print(list(nombres_con_vocal))
