#Ejercicio 4
#Importamos el math para el numero PI
import math 
#Pedimos el radio y lo definimos como variable
radio = float(input("Ingrese el radio del circulo: "))
#Calculamos el perimetro
perimetro = 2 * radio * math.pi 
#Calculamos area
area = math.pi * radio ** 2 
#Mostramos resultados 
print(f"El perimetro es: {perimetro}, y el area es {area}")