# Defino funcion
def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Pido datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
# Llamo a la funcion
print(informacion_personal(nombre, apellido, edad, residencia))