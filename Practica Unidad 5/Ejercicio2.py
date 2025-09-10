#Creo la lista
lista = []
#Pedimos al usuario que cargue 5 peoductos
for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    lista.append(producto)
#Mostramos lista ordenada
print(sorted(lista))
#Pedimos si desea eliminar algo
eliminar = input("¿Que producto desea eliminar? " \
"Si no desea eliminar ninguno ingrese 0: ")
if eliminar in lista:
    lista.remove(eliminar)
#Pedimos si desea agregar algun producto
agregar = input("Ingrese el producto que desea agregar, " \
"Si no desea agregar un producto ingrese 0: ")
if agregar != "0":
    lista.append(agregar)
#Mostramos la lista final
print(sorted(lista))