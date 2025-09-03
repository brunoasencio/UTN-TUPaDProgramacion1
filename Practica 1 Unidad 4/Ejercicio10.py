# Pedimos el número al usuario
num = int(input("Ingrese un número entero: "))
num_invertido = 0
n = abs(num) 

while n > 0:
    #Tomamos el ultimo digito
    digito = n % 10 
    #Agregamos el dígito al nuevo número
    num_invertido = num_invertido * 10 + digito
    #Eliminamos el último dígito
    n //= 10                
# Si el número original era negativo, lo hacemos negativo
if num < 0:
    num_invertido = -num_invertido
#Imprimimos resultado
print("El número invertido es:", num_invertido)
