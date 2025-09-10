#Creamos matiz
tateti = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
#Impimimos matiz
for i in range(len(tateti)):
    print(tateti[i])
#Creamos variable finalizar y signo
finalizar = 9 
for a in range(finalizar):        #Creamos for para el "Juego"
    if a % 2 == 0:                #Si es par el signo es X sino O, asi es una vez y una vez 
        signo = "X"
    else:
        signo = "O"
    print("Si desea terminar ingrese 10")          #Pedimos donde desea ingresar el signo
    fila = int(input(f"Ingrese en qué fila desea añadir {signo}: "))
    print("Si desea terminar ingrese 10")
    fila -= 1                                      #Ajustamos indices
    if fila == 9:                                  #Si ingresa 10 finaliza el juego
        print("El juego a finalizado")                                  
        break
    columna = int(input(f"Ingrese en qué columna desea añadir {signo}: ")) 
    columna -= 1                                   #Ajustamos indices
    if columna == 9:                               #Si ingresa 10 finaliza el juego
        print("El juego a finalizado")                               
        break
    tateti[fila][columna] = signo
    for i in range(len(tateti)): 
        print(tateti[i])

