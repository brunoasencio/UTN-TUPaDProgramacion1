import math
# Defino la primer funcion
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area
# Defino la segunda funcion
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio 
    return perimetro
# Solicito el radio al usuario
radio = int(input("Ingrese el radio del circulo: "))
# Llamo a las funciones
perimetro = calcular_perimetro_circulo(radio)
area = calcular_area_circulo(radio)
# Imprimo resultados
print(f"El perimetro es: {round(perimetro, 2)}")
print(f"El area es: {round(area, 2)}")