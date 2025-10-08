# Diccionario
precio_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva":
1450} 
#--- Ejercicio 1 ---
# Agregar las frutas con sus precios
precio_frutas["Naranja"] = 1200
precio_frutas["Manzana"] = 1500
precio_frutas["Pera"] = 2300
# Comprobamos
print(f"Ejercicio 1: {precio_frutas}")

#--- Ejercicio 2 ---
# Actualizamos los precios
precio_frutas["Banana"] = 1330
precio_frutas["Manzana"] = 1700
precio_frutas["Melón"] = 2800
# Comprobamos
print(f"Ejercicio 2: {precio_frutas}")

#--- Ejercicio 3 ---
lista_sin_precios = [precio_frutas.keys()]
# Comprobamos
print(f"Ejercicio 3: {lista_sin_precios}")
