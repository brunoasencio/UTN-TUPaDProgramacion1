# Función para limpiar la palabra 
def limpiar_palabra(palabra):
    palabra = "".join(palabra.split())  # Quitar espacios
    # Quitar tildes
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    return palabra

 # Defino la funcion para verificar palíndromo
def es_palindromo(palabra):
    palabra = limpiar_palabra(palabra)
    if len(palabra) <= 1:
        return True 
    if palabra[0] != palabra[len(palabra) - 1]:
        return False
    else:
       return es_palindromo(palabra[1:len(palabra) - 1])

# Pido al usuario la palabra
palabra = input("Ingrese una palabra: ")

# Llamo a la funcion
respuesta = es_palindromo(palabra)

# Muestro resultados
if respuesta == False:
    print(f"{palabra} no es Palindromo")
else:
    print(f"{palabra} es Palindromo")