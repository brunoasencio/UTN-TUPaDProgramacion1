#Creamos la lista anidada y listas
matiz = [[7, 27], [8, 25], [10, 24], [11, 28], [13,23], [10, 25], [13, 26]]
minimas = []
maximas = []
amplitud_mayor = 0
dia = 0
#Creamos la matiz de 7x2
for i in range(len(matiz)):
    print(matiz[i])
    #Comprobamos cual es la mayor amplitud
    amplitud = matiz[i][1] - matiz[i][0]
    if amplitud > amplitud_mayor:
        amplitud_mayor = amplitud
        dia = i + 1
    #Sacamos minimas y maximas
    minimas.append(matiz[i][0])
    maximas.append(matiz[i][1])
#Sacamos promedios
promedio_max = sum(maximas) / len(maximas) 
promedio_min = sum(minimas) / len(minimas) 
#Mostramos resultados
print("El promedio de la maxima es:",round(promedio_max, 1),"y el de la minima es:",round(promedio_min, 1))
print("La mayor amplitud fue de:",amplitud_mayor,"en el dia:",dia,)