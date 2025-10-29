# Defino la funcion
def contar_bloques(n):
    if n == 1:           # Caso base
        return 1
    else:                # Caso recursivo
        return n + contar_bloques(n - 1)
    
# Pregunto número al usuario
n = int(input("Inrese el número de bloques en el nivel más bajo: "))

# Llamo a la funcion
resultado = contar_bloques(n)

# Imprimo resultados
print(f"La cantidad de bloques necesarios es: {resultado}")