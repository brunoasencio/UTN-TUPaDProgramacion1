#Definimos variables
suma_total = 0
promedio = 0
#Creamos el bucle que pida numeros
for i in range(0,100):
    num = int(input("Ingrese un número: "))
    #Sumamos numeros
    suma_total += num
#Calculamos promedio
promedio = suma_total / 100
#Mostramos resultado
print("La media de los números ingresados es de:",promedio)