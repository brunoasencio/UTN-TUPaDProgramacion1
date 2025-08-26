#Pedimos el nombre
nombre = input("Ingrese su nombre: ")
#Pedimos como lo quiere recibir
print("Si quiere su nombre en mayúsculas ingrese 1")
print("Si quiere su nombre en minúsculas ingrese 2")
print("Si quiere su nombre con la primera letra en mayúscula ingrese 3")
tipo = int(input("Ingrese el número: "))
#Verificamos e imprimimos resultados
if tipo == 1:
    print(nombre.upper())
elif tipo == 2:
    print(nombre.lower())
else:
    print(nombre.capitalize())