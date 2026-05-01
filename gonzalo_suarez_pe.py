
def validar_lista_vacia(lista_productos):

    if not lista_productos:
        print("Error, lista de productos vacia")
        return False
    return True

def pedir_cadena(mensaje, es_numero=False):
    while True:
        dato = input(mensaje).strip()
        if not dato:
            print("Error, este campo no puede estar vacio")
            continue
        
        if es_numero:
            if dato.isdigit():
                return int(dato)
            print("Error, debe ingresar un numero entero positivo")
        else:
            return dato.lower()

def pedir_datos_producto():
    print()
    nombre = pedir_cadena("Ingrese nombre del producto: ")
    categoria = pedir_cadena("Ingrese categoria del producto: ")
    precio = pedir_cadena("Ingrese precio del producto (sin centavos): ", es_numero=True)

    return [nombre,categoria,precio]

def agregar_producto(lista_productos):
    
    print("\n| --- Agregar Productos --- |")
    while True:
        nuevo_producto = pedir_datos_producto()
        lista_productos.append(nuevo_producto)

        opcion_usuario = input(f"Producto: {nuevo_producto[0]} cargado. Quiere cargar otro? si/no\n").lower()

        if opcion_usuario != "si":
            print("\n| --- Carga Exitosa --- |\n")
            break
    
def mostrar_productos(lista_productos,secciones):

    print("\n| --- Mostrar Productos --- |")

    if not validar_lista_vacia(lista_productos): return
    
    for i in range(len(lista_productos)):
        print(f"\nProducto {i+1}: ")
        for j in range(len(lista_productos[i])):
            print(f"{secciones[j]}: {lista_productos[i][j]}")

def buscar_producto(lista_productos,secciones):

    
    print("\n --- Productos encontrados --- ")
    
    if not validar_lista_vacia(lista_productos): return

    nombre_producto = pedir_cadena("Ingrese nombre del producto: ")
    encontrado = False

    for i in range(len(lista_productos)):
        for j in range(len(lista_productos[i])):
            if nombre_producto in lista_productos[i]:
                print(f"- {secciones[j]}: {lista_productos[i][j]}")
                encontrado= True
        print()

    if not encontrado:          
        print("\n| - No se encontro el producto - |\n")

def eliminar_producto(lista_productos,secciones):

    if not validar_lista_vacia(lista_productos): return

    mostrar_productos(lista_productos,secciones)

    posicion = pedir_cadena("\nIngrese el numero del producto a eliminar: ",True)
    indice = posicion - 1

    if indice >= 0 and indice < len(lista_productos):
        producto_eliminado = lista_productos.pop(indice)
        print(f"Producto: {producto_eliminado[0]} eliminado exitosamente")
    else:
        print("Error, producto no encontrado")

def menu_principal():

    lista_productos = []
    secciones = ["nombre","categoria","precio"]

    while True:

        print("\n--- Menu Principal ---")

        opcion_menu= pedir_cadena("1. Agregar Producto\n2. Mostrar Productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir\n-------------------\nIngrese opcion: ", es_numero=True)

        match(opcion_menu):
            case 1:
                agregar_producto(lista_productos)
            case 2:
                mostrar_productos(lista_productos,secciones)
            case 3:
                buscar_producto(lista_productos,secciones)
            case 4:
                eliminar_producto(lista_productos,secciones)
            case 5:
                print("cerrando programa...")
                break
            case _:
                print("Opcion incorrecta, reintente: ")
                

menu_principal()

