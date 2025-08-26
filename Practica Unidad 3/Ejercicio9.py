#Pedimos la magnitud del terremoto
terremoto = int(input("Ingrese la magnitud del terremoto: "))
#Verificamos e imprimimos resultados
if terremoto < 3:
    print("Muy leve")
elif terremoto >= 3 and terremoto < 4:
    print("Leve")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte")
elif terremoto >= 6 and terremoto < 7:
    print("Muy fuerte")
elif terremoto >= 7:
    print("Extremo")