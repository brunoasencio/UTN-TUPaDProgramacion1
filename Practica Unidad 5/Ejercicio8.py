#Creamos la matiz
notas = [[7, 8, 9], [9, 9, 3], [4, 5, 6]]
#Calculamos promedios
promedio_estudiante1 = sum(notas[0]) / 3
promedio_estudiante2 = sum(notas[1]) / 3
promedio_estudiante3 = sum(notas[2]) / 3
#Calculamos promedios de cada materia
promedio_materia1 = (notas[0][0] + notas[1][0] + notas[2][0]) / 3
promedio_materia2 = (notas[0][1] + notas[1][1] + notas[2][1]) / 3
promedio_materia3 = (notas[0][2] + notas[1][2] + notas[2][2]) / 3
#Mostramos resultados
print("El promedio del 1er estudiante es:",round(promedio_estudiante1, 1))
print("El promedio del 2do estudiante es:",round(promedio_estudiante2, 1))
print("El promedio del 3er estudiante es:",round(promedio_estudiante3, 1))
print("El promedio de la 1er materia es:",round(promedio_materia1, 1))
print("El promedio de la 2da materia es:",round(promedio_materia2, 1))
print("El promedio de la 3er materia es:",round(promedio_materia3, 1))