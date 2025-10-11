inventario = {}

while True:
    try:
        opcion = int(input("Sistema de gestión:\n 1- Añadir producto\n 2- Vender producto\n 3- Visualizar inventario\n 4- Salir\n"))
    except:
        ValueError("Tienes que escoger una opción de la 1 a la 4")

    match opcion: #es como un switch, permite ejecutar distintos bloques de codigo segun el valor de opcion
        case 1:
            nombre = input("Nombre del producto:\n")
            cantidad = int(input("Cantidad de unidades:\n"))
            inventario[nombre] = inventario.get(nombre, 0) + cantidad
            """inventario es un diccionario que guarda los productos y cuántas unidades hay
            nombre es la clave del producto (lo que escribe el usuario)
            cantidad es el número de unidades que se añaden
            get() es un método de los diccionarios que intenta obtener el valor asociado a una clave.
            Si la clave existe, devuelve su valor.
            Si la clave no existe, devuelve el valor por defecto que tú le indiques (en este caso, 0).
            Se suma la cantidad actual (si existe) con la nueva cantidad introducida."""
        case 2:
            nombre = input("Nombre del producto:\n")
            cantidad = int(input("Cantidad de unidades:\n"))
            stock = inventario.get(nombre)
            if stock == None:
                print("No existe el producto en el inventario")
            elif stock < cantidad:
                print("No existe suficiente cantidad en el inventario")
            else:
                inventario[nombre] = stock - cantidad
        case 3:
            if not inventario:
                print("Inventario vacío")
            else:
                for producto, cantidad in sorted(inventario.items()):
                    print(f"{producto}: {cantidad} unidades")
            """🔸 Si el inventario no está vacío, entra en el else y muestra su contenido.
               🔸 Si sí está vacío, imprime "Inventario vacío"
               El método .items() devuelve todos los pares (clave, valor) del diccionario, pero en formato especial llamado tuplas.
               Es decir, cada elemento es una pareja (producto, cantidad).
               La función sorted() ordena los elementos.Por defecto, ordena por el primer elemento de cada tupla
               Este bucle recorre cada par (clave, valor) del diccionario ordenado
               """
        case 4:
            print("Bye bye hasta otro ratito")
            exit()