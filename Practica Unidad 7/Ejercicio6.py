# Diccionario para guardar notas
alumnos = {}
for i in range(1, 4):
    alumno_nuevo = input(f"Ingrese el nombre del alumno {i}: ")
    # Verifico si el nombre es repetido
    while alumno_nuevo in alumnos:
        print(f"El alumno {alumno_nuevo} ya esta registrado. Intente de nuevo")
        alumno_nuevo = input(f"Ingrese el nombre del alumno {i}: ")
    # Una vez que no es repetido lo agregamos al diccionario
    alumnos[alumno_nuevo] = ()
for i in alumnos:           # Pedimos 3 notas por alumno
    nota1 = float(input(f"Ingrese la primer nota de {i}: "))
    nota2 = float(input(f"Ingrese la segunda nota de {i}: "))
    nota3 = float(input(f"Ingrese la tercer nota de {i}: "))
    alumnos[i] = (nota1, nota2, nota3)        # Las agregamos en forma de tupla
for i in alumnos:
    temporal = alumnos[i]
    promedio = sum(temporal) / 3                  # Calculamos promedio
    print(f"El promedio de {i} es: {round(promedio, 2)}")        # Mostramos promedio
