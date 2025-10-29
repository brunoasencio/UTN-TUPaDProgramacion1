# Defino la funcion
def contar_digito(numero, digito):
    if numero == 0:                                        # Caso base
        return 0
    ultimo_digito = numero % 10                            # Obtengo el ultimo número
    if ultimo_digito == digito:                            
        return 1 + contar_digito(numero // 10, digito)     # Caso recursivo
    else:
        return contar_digito(numero // 10, digito)
    
# Solicito al usuario
numero = int(input("Ingrese un número: "))

# Verifico que haya ingresado del 1 al 9
while True:
    digito = int(input("Ingrese un digito del 0 al 9: "))
    if digito >= 0 and 9 >= digito:
        break
    else:
        print("Número no valido (del 0 al 9).")
        continue 

# Llamo a la funcion
resultado = contar_digito(numero, digito)

# Imprimo resultados
print(f"El {digito} aparece {resultado} veces en el número {numero}")