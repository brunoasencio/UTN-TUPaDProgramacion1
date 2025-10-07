# Defino la funcion
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")
# Solicito grados
celsius = int(input("Ingrese cuantos grados celsius desea convertir: "))
# Llamos a la funcion
celsius_a_fahrenheit(celsius)