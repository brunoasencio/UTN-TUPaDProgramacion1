# Lista para guardar los productos
productos = []

# Abro el archivo en modo lectura
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()       # Elimina espacios y saltos de línea
        datos = linea.split(",")    # Separa por coma
        
        # Creo un diccionario para cada producto
        producto = {
            "nombre": datos[0],
            "precio": datos[1],   
            "cantidad": datos[2]   
        }
        
        # Agrego el diccionario a la lista
        productos.append(producto)

# Muestro la lista de diccionarios
for p in productos:
    print(p)