# Lista para guardar los productos
productos = []
encontrado = False
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
# Le pido al usuario que ingrese el nombre de un producto
producto_usuario = input("Ingrese el nombre de un producto: ")
for producto in productos:       # Recorro todos los productos comparandolo con el del usuario
    if producto['nombre'].lower() == producto_usuario.lower():  # Ignora mayúsculas/minúsculas
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:         # Si no se encontro, muestro mensaje de error
    print(f"{producto_usuario} no esta registrado.")