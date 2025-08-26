contraseña = input("Ingrese una contraseña: ")
longi = len(contraseña)
if longi >= 8 and longi <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")