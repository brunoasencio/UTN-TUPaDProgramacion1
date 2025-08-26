#Pedimos la palabra
palabra = input("Ingrese una palabra o frase: ")
#Definimos la ultima letra
ultima_letra = palabra[-1]
#Verificamos si es vocal e imprimimos resultado
if ultima_letra in "aeiou":
    palabra = palabra + "!"
    print(palabra)
else:
    print(palabra)