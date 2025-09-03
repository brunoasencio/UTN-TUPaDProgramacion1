#Solicitamos el numero
num = int(input("Ingrese un número entero: "))
digitos = 0
#Comprobamos si es 0
if num == 0:
    digitos += 1
#Calculamos digitos
while num > 0:
    digitos += 1
    num //= 10
#Imprimimos resultado
print("El número que ingresaste tiene",digitos,"digito/s")