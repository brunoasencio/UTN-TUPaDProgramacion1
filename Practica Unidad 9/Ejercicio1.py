# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Pido al usuario un número
num = int(input("Introduce un número entero: "))

# Calculo y muestro el factorial de todos los números desde 1 hasta num
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")