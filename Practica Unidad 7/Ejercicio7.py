# Creamos los sets con nombres de los que aprobaron
parcial1 = {"Ana", "Luis", "Carla", "Diego"}
parcial2 = {"Luis", "Carla", "Marcos", "Elena"}
# Muestro los que aprobaron ambos
ambos = parcial1 & parcial2
print("Aprobó ambos parciales:", ambos)
# Muestro los que solo aprobaron uno de los dos
solo_uno = parcial1 ^ parcial2
print("Aprobó solo uno de los parciales:", solo_uno)
# Muestro los que aprobaron un parcial al menos
al_menos_uno = parcial1 | parcial2
print("Aprobó al menos un parcial:", al_menos_uno)
