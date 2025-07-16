productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["Lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX 1050"],
    "FS1230HD": ["Acer", 15.6, "4GB", "DD", "1T", "Intel Core i3", "integrada"]
}

stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "GF75HD": [749990, 2],
    "123FHD": [290890, 32],
    "342FHD": [444990, 7],
    "UWU131HD": [349990, 1],
    "FS1230HD": [249990, 0]
}

def stock_marca(nombre_marca):
    nombre_marca = nombre_marca.lower()
    total_stock = 0
    for modelo, detalles in productos.items():
        marca_actual = detalles[0].lower()
        if marca_actual == nombre_marca:
            total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")

def busqueda_precio(precio_minimo, precio_maximo):
    modelos_en_rango = []
    for modelo, datos_stock in stock.items():
        precio_actual = datos_stock[0]
        cantidad_disponible = datos_stock[1]
        if precio_minimo <= precio_actual <= precio_maximo and cantidad_disponible > 0:
            nombre_marca = productos[modelo][0]
            modelos_en_rango.append(f"{nombre_marca}–{modelo}")
    if modelos_en_rango:
         
        modelos_en_rango.sort()
        print(f"Los notebooks entre los precios consultados son: {modelos_en_rango}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(nombre_modelo, nuevo_precio):
    if nombre_modelo in stock:
        stock[nombre_modelo][0] = nuevo_precio
        return True
    else:
        return False

def mostrar_menu():
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.", "2. Búsqueda por precio.", "3. Actualizar precio.", "4. Salir.")

def main():
    while True:
        mostrar_menu()
        opcion_seleccionada = input("Ingrese opción: ")

        if opcion_seleccionada == "1":
            marca_ingresada = input("Ingrese marca a consultar: ")
            stock_marca(marca_ingresada)

        elif opcion_seleccionada == "2":
            while True:
                try:
                    precio_minimo = int(input("Ingrese precio mínimo: "))
                    precio_maximo = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(precio_minimo, precio_maximo)

        elif opcion_seleccionada == "3":
            while True:
                modelo_ingresado = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un valor numérico para el precio.")
                    continue

                resultado_actualizacion = actualizar_precio(modelo_ingresado, nuevo_precio)

                if resultado_actualizacion:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
                if respuesta != "s":
                    break

        elif opcion_seleccionada == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

main()
