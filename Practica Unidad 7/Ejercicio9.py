# Agenda 
agenda = {
    ("Lunes", "09:00"): "Reunión con el equipo",
    ("Martes", "14:00"): "Clase de Python",
    ("Miércoles", "11:30"): "Cita médica",
    ("Viernes", "16:00"): "Entrega de proyecto"
}

# Consulta de evento
dia = input("Ingrese el día a consultar: ").capitalize()
hora = input("Ingrese la hora a consultar (ej: 09:00): ")

clave = (dia, hora)
# Muestro resultado
if clave in agenda:
    print(f"En {dia} a las {hora} hay: {agenda[clave]}")
else:
    print(f"No hay ningún evento registrado en {dia} a las {hora}.")
