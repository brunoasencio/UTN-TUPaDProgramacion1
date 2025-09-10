#Creamos la lista con notas de 10 estudiantes
notas = [9,8.5,3,5,7,8,9.5,10,6,5]
#Muestro la lista completa
print(notas)
#Calculamos promedio
promedio = sum(notas)
promedio = promedio / 10
#Mostramos el resultado del promedio
print(promedio)
#Comprobamos nota mas baja y mas alta
for indice_pasada in range(10 - 1):
    for indice_actual in range(10 - 1 - indice_pasada):
        if notas[indice_actual] > notas[indice_actual + 1]:
            notas[indice_actual], notas[indice_actual + 1] = notas[indice_actual + 1], notas[indice_actual]
nota_alta = notas[9]
nota_baja = notas[0]
#Imprimimos notas
print(nota_alta)
print(nota_baja)