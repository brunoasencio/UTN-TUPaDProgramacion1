hemisferio = input("Ingrese el hemisferioen el que se encuentra(N/S): ")
mes = input("Ingrese en que mes del año: ")
dia = int(input("Ingrese dia(en número): "))
if mes.capitalize() == "Diciembre" and dia >= 21 or mes.capitalize() == "Marzo" and dia <= 20:
    if hemisferio.capitalize() == "Norte":
        print("Invierno")
    else:
        print("Verano")
elif mes.capitalize() == "Marzo" and dia >= 21 or mes.capitalize() == "Junio" and dia <= 20:
    if hemisferio.capitalize() == "Norte":
        print("Primavera")
    else:
        print("Otoño")
elif mes.capitalize() == "Junio" and dia >= 21 or mes.capitalize() == "Septiembre" and dia <= 20:
    if hemisferio.capitalize() == "Norte":
        print("Verano")
    else:
        print("Invierno")
elif mes.capitalize() == "Septiembre" and dia >= 21 or mes.capitalize() == "Diciembre" and dia <= 20:
    if hemisferio.capitalize() == "Norte":
        print("Otoño")
    else:
        print("Primavera")