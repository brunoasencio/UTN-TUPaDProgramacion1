#Creamos variables
num = 1
resultado = 0 
#Creamos el bucle para que ingrese los numeros
while num != 0:
    print("Ingrese el número")
    print("Si desea frenar ingrese 0")
    num = int(input())
    resultado += num
#Mostramos resultado
print("El resultado de la suma de los números ingresados es:",resultado)