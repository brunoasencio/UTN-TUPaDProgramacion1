#Definimos variables
num_par = 0
num_impar = 0
num_positivo = 0
num_negativo = 0
num_cero = 0
#Creamos el bucle que pida número
for i in range(0,100):
    num = int(input("Ingrese un número: "))
    #Comprobamos si es par
    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1
    #Comprobamos si es positivo
    if num > 0:
        num_positivo += 1
    elif num < 0:
        num_negativo += 1
    else:
        num_cero += 1
#Imprimimos resultados
print("Ingresate",num_par,"números pares",num_impar,"números impares",num_positivo,"números positivos",num_negativo,"números negativos",num_cero,"ceros")