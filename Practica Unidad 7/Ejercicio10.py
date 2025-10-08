# Diccionario original
paises = {
    "mexico": "ciudad de mexico",
    "francia": "parís",
    "japon": "tokio",
    "canada": "ottawa"
}
# Diccionario invertido
capitales = {
    "ciudad de mexico": "mexico",
    "parís": "francia",
    "tokio": "japon",
    "ottawa": "canada"
}
# Muestro ambos diccionarios
print("Diccionario original:")
for pais, capital in paises.items():
    print(f"[{pais}: {capital}]")

print("Diccionario invertido")
for capital, pais in capitales.items():
    print(f"[{capital}: {pais}]")