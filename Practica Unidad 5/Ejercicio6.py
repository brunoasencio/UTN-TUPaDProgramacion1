#Creo la lista
lista = [1, 2, 3, 4, 5, 6, 7]
#Guardamos el ultimo valor
ultimo = lista[6]
#Movemos todos una posicion a la derecha
for i in range(len(lista)-1, 0, -1):
    lista[i] = lista[i - 1] 
#Agregamos el ultimo valor al principio
lista[0] = ultimo
#Mostramos la lista final
print(lista)