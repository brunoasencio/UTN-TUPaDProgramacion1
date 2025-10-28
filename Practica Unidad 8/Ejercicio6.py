# ============================================
# Ejercicio 1
# ============================================
# Creo/abro el archivo
with open("productos.txt", "w") as  archivo:
    archivo.write("Lapicera,35,25\n")         # Agrego primer producto
    archivo.write("Computadora,350,10\n")     # Agrego segundo producto
    archivo.write("Buzo,200,30\n")            # Agrego tercer producto


# ============================================
# Ejercicio 2
# ============================================
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


# ============================================
# Ejercicio 3
# ============================================
# Le pido que ingrese un nuevo producto
nuevo = input("Ingrese un nuevo producto (nombre,precio,cantidad): ").strip()
with open("productos.txt", "a") as archivo:
    archivo.write("\n" + nuevo)


# ============================================
# Ejercicio 4
# ============================================
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


# ============================================
# Ejercicio 5
# ============================================
# Le pido al usuario que ingrese el nombre de un producto
producto_usuario = input("Ingrese el nombre de un producto: ")
encontrado = False
for producto in productos:       # Recorro todos los productos comparandolo con el del usuario
    if producto['nombre'].lower() == producto_usuario.lower():  # Ignora mayúsculas/minúsculas
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:         # Si no se encontro, muestro mensaje de error
    print(f"{producto_usuario} no esta registrado.")


# ============================================
# Ejercicio 6
# ============================================
# Después de haber leído, buscado o agregado productos, sobrescribo el archivo productos.txt
# escribiendo nuevamente todos los productos actualizados desde la lista.

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\n Archivo 'productos.txt' actualizado correctamente con todos los productos actuales.")
