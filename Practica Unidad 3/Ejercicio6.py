#Creamos la lista de números aleatorios
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Sacamos la Moda, Media y Mediana
from statistics import mode, median, mean
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#Verificamos e imprimimos resultados
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")