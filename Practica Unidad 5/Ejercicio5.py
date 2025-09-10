#Creamos lista
lista = ["Juan", "Bruno", "Pedro", "Mateo", "Gabriel", "Manuel", "Francisco", "Bautista"]
#Preguntamos si desea agregar o eliminar
accion = input("¿Desea agregar o eliminar?, Si no quiere realizar ninguna de las dos ingrese `No´ ")
if accion.capitalize() == "Agregar":
    agregar = input("Ingrese que nombre desea agregar: ")
    lista.append(agregar)
elif accion.capitalize() == "Eliminar":
    eliminar = input("Ingrese que nombre desea eliminar: ")
    if eliminar in lista:
        lista.remove(eliminar)
#Mostramos la lista final
print(lista)