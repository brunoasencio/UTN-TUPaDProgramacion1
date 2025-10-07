# Defino la funcion
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del: {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
# Solicito el numero
numero = int(input("Ingrese el numero que desea ver la tabla: "))
# Llamo a la funcion
tabla_multiplicar(numero)