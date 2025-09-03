#Pedimos el numero y definimos "resultado"
num = int(input("Ingrese un número positivo: "))
resultado = 0
#Creamos un bucle que sume desde el 0 hasta el numero
for i in range(0, num + 1):
    resultado += i
#Mosramos resultados
print("La suma de todos los números comprendidos entre 0 y el número ingresado es:",resultado)