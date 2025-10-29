# Defino la funcion que sume los digitos
def suma_digitos(n):
    if n == 0:               # Caso base
        return 0 
    else:                    # Caso recursivo
        return n % 10 + suma_digitos(n // 10)
    
# Solicito al usuario que ingrese el número
n = int(input("Ingrese el número que desea sumar sus digitos: "))

# Llamo a la funcion
resultado = suma_digitos(n)

# Imprimo resultados
print(f"El resultado es: {resultado}")