# Defino funcion
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
# Solicito numeros
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
# Llamamos a la funcion e imprimimos
print(f"El promedio de los 3 numeros es: {calcular_promedio(a, b, c)}")