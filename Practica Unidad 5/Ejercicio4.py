#Creamos listas
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_final = []
#Comprobamos si esta repetido y si no esta lo agregamos
for i in range(len(datos)):
    if datos[i] in lista_final:
        pass
    else:
        lista_final.append(datos[i])
#Mostramos lista final
print(lista_final)