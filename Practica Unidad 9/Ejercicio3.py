# Defino funcion
def funcion(n, m):
    if m == 0:                 # Caso base
        return 1
    else:                      # Caso recursivo
        return n * funcion(n, m - 1)

# Algoritmo general para probar la función
def general():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = funcion(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")

# Llamada al algoritmo principal
general()