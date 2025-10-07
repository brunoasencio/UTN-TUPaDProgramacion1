# Defino la función
def tabla_multiplicar(numero):
    resultado = f"Tabla de multiplicar del {numero}:\n"
    for i in range(1, 11):
        resultado += f"{numero} x {i} = {numero * i}\n"
    return resultado

# Solicito el número
numero = int(input("Ingrese el numero que desea ver la tabla: "))

# Llamo a la función y muestro el resultado
print(tabla_multiplicar(numero))