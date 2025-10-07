# Defino la funcion
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
# Solicito al usuario que ingrese los segundos
segundos = int(input("Ingrese los segundos: "))
# Llamo a la funcion e imprimo resultado
print(f"En {segundos} segundos hay {segundos_a_horas(segundos)} hora/s")
