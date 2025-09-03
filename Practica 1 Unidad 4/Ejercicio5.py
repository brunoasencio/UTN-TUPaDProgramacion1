#Creamos el numero aleatorio
import random
num_aleatorio = random.randint(0,9)
#Definimos las variables
num = 10
intentos = 1
#Primer intento
num = int(input("Adivina el número entre 0 y 9: "))
#Bucle hasta que adivinw wl numero, contando intentos
while num != num_aleatorio:
    num = int(input("Incorrecto, intenta otra vez: "))
    intentos += 1
print("¡Correcto! El número es",num_aleatorio,"lo lograste en",intentos,"intentos" )