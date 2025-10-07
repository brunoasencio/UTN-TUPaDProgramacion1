# Defino la funcion
def saludar_usuario(nombre):       
    return (f"Hola {nombre}!")             # Saludo
 # Pido el nombre
nombre = input("Ingrese su nombre: ")
# Llamo a la funcion
print(saludar_usuario(nombre))
