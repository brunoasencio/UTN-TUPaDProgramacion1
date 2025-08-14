#Ejercicio 1 
print("Hola Mundo!")

#Ejercicio 2
#Pedimos que ingrese el nombre y definimos la variable
nombre1 = input("Ingrese su nombre: ")
#Saludamos con el nombre
print(f"¡Hola, {nombre1}!")

#Ejercicio 3
#Pedir datos al usuario y lo definimos como variable
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_de_residencia = input("Ingresa tu lugar de residencia: ")
#Mostramos mensaje final
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

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

#Ejercicio 5 
#Pedimos segundos y lo definimos como variable
segundos = float(input("Ingrese la cantidad de segundos que quiere convertir: "))
#Calculamos horas
horas = round(segundos / 3600, 2)
#Mostramos horas
print(f"¨{segundos} segundos son igual a {horas} hora/s")

#Ejercicio 6 
#Pedimos que ingrese un número
numero = int(input("Ingrese un número entero: "))
#Multiplicamos
tabla0 = numero * 0
tabla1 = numero * 1
tabla2 = numero * 2
tabla3 = numero * 3
tabla4 = numero * 4
tabla5 = numero * 5
tabla6 = numero * 6
tabla7 = numero * 7
tabla8 = numero * 8
tabla9 = numero * 9
tabla10 = numero * 10
#Mostramos resultados
print(f"""
{numero} x 0 = {tabla0}
{numero} x 1 = {tabla1}
{numero} x 2 = {tabla2}
{numero} x 3 = {tabla3}
{numero} x 4 = {tabla4}
{numero} x 5 = {tabla5}
{numero} x 6 = {tabla6}
{numero} x 7 = {tabla7}
{numero} x 8 = {tabla8}
{numero} x 9 = {tabla9}
{numero} x 10 = {tabla10}
""")

#Ejercicio 7
#Pedimos números y los definimos
numero1 = float(input("Ingrese un número diferente a 0: "))
numero2 = float(input("Ingrese otro número diferente a 0: "))
#Hacemos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
#Mostramos resultados
print(f"""
suma: {suma}
resta: {resta}
multiplicación: {multiplicacion}
division: {division}
""")

#Ejercicio 8 
#Pedimos datos y los definimos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
#Calculamos IMC
imc = round(peso / altura ** 2)
#Mostramos resultados
print(f"Su IMC es de: {imc}")

#Ejercicio 9 
#Pedimos temperatura y la definimos
celcius = float(input("Ingrese la temperatura en grados Celcius: "))
#Transformamos a grados Fahrenheit
fahrenheit =round((9 / 5) * celcius + 32)
#Mostramos resultado
print(f"{celcius} °C equivalen a {fahrenheit} °F") 

#Ejercicio 10 
#Pedimos números y los definimos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
#Calculamos promedio
promedio = (num1 + num2 + num3) / 3
#Mostramos resultados
print(f"El promedio es: {promedio}")