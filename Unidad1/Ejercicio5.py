#Ejercicio 5 
#Pedimos segundos y lo definimos como variable
segundos = float(input("Ingrese la cantidad de segundos que quiere convertir: "))
#Calculamos horas
horas = round(segundos / 3600, 2)
#Mostramos horas
print(f"¨{segundos} segundos son igual a {horas} hora/s")