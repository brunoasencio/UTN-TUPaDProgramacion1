#Importamos para generar números aleatorios
import random
#Generamos la lista con números aleatorios
lista = [random.randint(1,100) for _ in range(15)]
#creamos lista para pares e impares
numeros_par = []
numeros_impar = []
#Comprobamos numeros pares e impares
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        numeros_par.append(lista[i])
    else:
        numeros_impar.append(lista[i])
#Muestro resultados
print("Hay",len(numeros_par),"números pares: ",numeros_par)
print("Hay",len(numeros_impar),"números impares: ",numeros_impar)