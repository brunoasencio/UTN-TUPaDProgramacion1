agenda = {}     # Diccionario para almacenar
# Bucle para consultar los contactos y el numero
for i in range(1,2):
        nombre = input("Ingrese el nombre del contacto que desea agregar: ")
        num = int(input(f"Ingrese el numero de {nombre}: "))
        if nombre in agenda:
            while nombre in agenda:
                print("Ese contacto ya existe. Intente de nuevo")
                nombre = input("Ingrese el nombre del contacto que desea agregar: ")
                num = int(input(f"Ingrese el numero de {nombre}: "))
            agenda[nombre] = num
            print(f"{nombre} agregado correctamente!")
        else:
            agenda[nombre] = num
            print(f"{nombre} agregado correctamente!")
# Bucle para el programa
while True:
    print("----------")
    print("1- Cargar nuevo contacto")
    print("2- Consultar por contacto")
    print("3- Salir del programa")
    print("----------")
    opcion = int(input("Ingrese que desea hacer: "))
    if opcion == 1:
            nombre = input("Ingrese el nombre del contacto que desea agregar: ")
            num = int(input(f"Ingrese el numero de {nombre}: "))
            if nombre in agenda:
                print("Ese contacto ya existe. Intente de nuevo")
                continue
            else:
                agenda[nombre] = num
                print(f"{nombre} agregado correctamente!")
    elif opcion == 2:
        nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")
        if nombre_consulta in agenda:
            print(f"{nombre_consulta}: {agenda[nombre_consulta]}")
        else:
            print("Ese nombre no existe en tu agenda.")
            continue
    else:
        print("Chau!")
        break