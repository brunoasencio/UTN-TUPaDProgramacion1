#Ejercicio 8 
#Pedimos datos y los definimos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
#Calculamos IMC
imc = round(peso / altura ** 2)
#Mostramos resultados
print(f"Su IMC es de: {imc}")