# Abro el archivo en modo lectura
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Quito espacios y saltos de línea
        linea = linea.strip()
        # Separo los datos por coma
        datos = linea.split(",")
        
        # Asigno cada dato a una variable
        producto = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        
        # Muestro en el formato deseado
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")
# Le pido que ingrese un nuevo producto
nuevo = input("Ingrese un nuevo producto (nombre,precio,cantidad)")
with open("productos.txt", "a") as archivo:
    archivo.write("\n" + nuevo)