# Set para almacenar frase
palabras_unicas = set()
# Diccionario para cantidades
cantidades = {}
# Lista para luego recorrer palabra por palabra
palabra_por_palabra = []
# Pido la frase
frase = input("Ingrese una frase: ")
# Separo en palabras
palabra_por_palabra = frase.split()
# Recorro contando cantidad, anoto los resultados en el diccionario y agrego set si no esta
palabra_por_palabra = frase.split()     
for i in palabra_por_palabra:
    if i not in cantidades:
        cantidades[i] = 1                  # Si no esta agrego 1 en el contador
        palabras_unicas.add(i)             # Como no esta la agrego al set
    else:
        cantidades[i] += 1                 # Si esta solamente agrego 1 al contador
# Imprimo resultados
print(palabras_unicas)
print(cantidades)