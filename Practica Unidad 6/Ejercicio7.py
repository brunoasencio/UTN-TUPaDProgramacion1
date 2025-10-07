# Defino la funcion
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"
    return (suma, resta, multiplicacion, division)
# Solicito los valores
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
# Llamo a la funcion
resultados = operaciones_basicas(a, b)
# Imprimo resultados
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")