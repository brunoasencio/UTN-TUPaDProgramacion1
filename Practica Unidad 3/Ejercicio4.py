#Pedimos la edad
edad = int(input("Ingrese su edad: "))
#Verificamos e imprimimos resultados
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")