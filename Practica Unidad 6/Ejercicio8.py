# Defino funcion
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
# Solicito los datos
altura = float(input("Ingrese su altura en cm: ")) / 100
peso = float(input("Ingrese su peso en kg: "))
# Llamo a la funcion e imprimo reusltado
print(f"Su imc es: {round(calcular_imc(peso, altura), 2)}")
