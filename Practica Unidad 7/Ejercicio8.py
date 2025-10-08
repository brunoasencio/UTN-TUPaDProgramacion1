stock = {}  # Declaramos fuera del bucle para mantener los datos

while True:
    menu = [       
        "-------------------",
        "1. Consultar stock",
        "2. Agregar unidades",
        "3. Agregar producto",
        "4. Salir",
        "-------------------"
    ]
    
    for i in menu:
        print(i)
        
    opcion = int(input("Ingrese la opción deseada: "))
    
    while opcion > 4 or opcion < 1:
        opcion = int(input("Opción no válida. Intente de nuevo: "))

    match opcion:
        case 1:
            print("Productos disponibles:", list(stock.keys()))
            producto = input("Ingrese el producto que desea consultar: ").capitalize()
            if producto in stock:
                print(f"Hay {stock[producto]} unidades de {producto}.")
            else:
                print(f"{producto} no está registrado.")
                
        case 2:
            if stock:
                print("Productos disponibles:", list(stock.keys()))
                producto = input("Ingrese el producto al que desea agregar stock: ").capitalize()
                if producto in stock:
                    cantidad = int(input("Ingrese la cantidad de unidades: "))
                    stock[producto] += cantidad
                    print(f"Se agregaron {cantidad} unidades de {producto}.")
                else:
                    print(f"{producto} no está registrado.")
            else:
                print("No hay productos registrados.")
                
        case 3:
            producto = input("Ingrese el nombre del producto a agregar: ").capitalize()
            if producto not in stock:
                cantidad = int(input("Ingrese la cantidad de unidades: "))
                stock[producto] = cantidad
                print(f"{producto} registrado con éxito con {cantidad} unidades.")
            else:
                print(f"{producto} ya está registrado.")
                
        case 4:
            print("Chau!")
            break
