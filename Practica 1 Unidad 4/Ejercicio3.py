#Pedimos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = 0
#Comprobamos cual es mayor
if num1 > num2:
    num1, num2 = num2, num1
for i in range(num1 + 1, num2):
    num1 += 1
    resultado += num1
#Imprimimos resultado
print("El resultado es",resultado)