# Defino la funcion Fibonacci
def fibonacci(n):
    if n <= 0:        # Caso base
        return 0
    elif n == 1:
        return 1
    else:            # Caso recursivo
        return fibonacci(n-1) + fibonacci(n-2)
    
# Pregunto al usuario hasta que posicion
n = int(input("¿Cuántos numeros de Fibonacci quieres ver?: "))

# Calculo hasta esa posicion
for i in range(n):
    print(fibonacci(i), end=" ")