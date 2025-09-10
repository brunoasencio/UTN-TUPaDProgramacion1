#Creamos la matiz
ventas = [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]
]
producto1 = 0
producto2 = 0
producto3 = 0
producto4 = 0
producto1_semanal = 0
producto2_semanal = 0
producto3_semanal = 0
producto4_semanal = 0
mayor_venta = 0
dia = 0
#Creamos el for de los 7 dias
for i in range(7):
    print("Ingrese las ventas del dia",i + 1,)
    #Para ingresar las ventas y sumar las ventas de cada producto en la semana
    producto1 = int(input("Producto 1: "))
    producto1_semanal += producto1
    ventas[0][i] = producto1      #Sumamos las ventas a la matix
    producto2 = int(input("Producto 2: "))
    producto2_semanal += producto2
    ventas[1][i] = producto2      #Sumamos las ventas a la matix
    producto3 = int(input("Producto 3: "))
    producto3_semanal += producto3
    ventas[2][i] = producto3      #Sumamos las ventas a la matix
    producto4 = int(input("Producto 4: "))
    producto4_semanal += producto4
    ventas[3][i] = producto4      #Sumamos las ventas a la matix
    #Comprobamos que dia fue el que mas se vendio
    venta_diaria = producto1 + producto2 + producto3 + producto4
    if venta_diaria > mayor_venta:
        mayor_venta = venta_diaria
        dia = i + 1
#Comprobamos que producto fue el que mas se vendio
totales_productos = [producto1_semanal, producto2_semanal, producto3_semanal, producto4_semanal]
producto_vendido = totales_productos.index(max(totales_productos)) + 1
#Imprimimos resultados de la venta de cada producto
print("El total de ventas del producto 1 fue:", producto1_semanal)
print("El total de ventas del producto 2 fue:", producto2_semanal)
print("El total de ventas del producto 3 fue:", producto3_semanal)
print("El total de ventas del producto 4 fue:", producto4_semanal)
#Imprimimos el dia que mas se vendio
print("El dia que más se vendio fue:",dia)
#Imprimimos el producto que mas se vendio
print("El producto que más se vendio es:",producto_vendido)