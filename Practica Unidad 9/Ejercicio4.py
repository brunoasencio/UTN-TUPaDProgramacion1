# Función recursiva que convierte entero a binario
def binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return binario(num // 2) + str(num % 2)

# Pregunto al usuario
num = int(input("Ingrese el número que desea convertir a binario: "))

# Llamo a la función
binario_texto = binario(num)

# Muestro resultados
print(f"El binario de {num} es: {binario_texto}")
