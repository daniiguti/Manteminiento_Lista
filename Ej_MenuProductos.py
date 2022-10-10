productos = []
#Metodos auxiliares
#Función para mostrar los productos con ese precio
def mostrarPrecioProductos(precioProducto):
    for i in range(len(productos)):
        if(productos[i]["Precio"] == precioProducto):
            print(productos[i])

#Función para comprobar si existe el precio de un articulo
def comprobarExistePrecioProducto(precioProducto):
    existe = False
    for i in range(len(productos)):
        if(productos[i]["Precio"] == precioProducto):
            existe = True
    return existe

#Función para mostrar los productos con ese nombre
def mostrarNombreProductos(nombreProducto):
    for i in range(len(productos)):
        if(productos[i]["Nombre"] == nombreProducto):
            print(productos[i])

#Función para comprobar si existe el nombre de artículo
def comprobarExisteNombreProducto(nombreProducto):
    existe = False
    for i in range(len(productos)):
        if(productos[i]["Nombre"] == nombreProducto):
            existe = True
    return existe

#Función para devolver en que posición de la lista
#esta el producto
def devolverIndiceProducto(codArticulo):
    for i in range(len(productos)):
        if (productos[i]["codArticulo"] == codArticulo):
            break
    return i

#Función para comprobar si existe el codigo de articulo
def comprobarExisteProducto(codArticulo):
    existe = False
    for i in range(len(productos)):
        if(productos[i]["codArticulo"] == codArticulo):
            existe = True
    return existe

#Función para pedir los datos modificables (nombre, descripcion y precio)
#También comprobamos que no se inroduzca nada
def pedirDatos():
    while True:
        nombre = input("Introduzca el nombre del producto: ")
        if(len(nombre) == 0):
            print("Introduzca un nombre correcto")
        else:
            break

    while True:
        descripcion = input("Introduzca la descripción: ")
        if(len(descripcion) == 0):
            print("Introduzca una descripción correcta")
        else:
            break

    while True:
        precio = input("Introduzca el precio: ")
        if(precio.isdigit() == False):
            print("Introduzca un número")
        else:
            break

    return nombre, descripcion, precio

#Metodos de las opciones posibles
#Método de alta, pedimos el codigo de articulo, comprobamos que NO existe
#y hasta que no introduzca uno correcto no vamos a dejar que salga
#una vez introducido uno correcto, pedimos los datos y añadimos un diccionario
#a la lista
def altaProducto():
    codigoArticulo = 0
    while True:
        codigoArticulo = input("Introduzca el codigo de articulo: ")
        if(comprobarExisteProducto(codigoArticulo) == True):
            print("Ya existe ese código, introduzca otro distinto")
        else:
            break

    nombre, descripcion, precio = pedirDatos()

    producto = {
        "codArticulo": codigoArticulo,
        "Nombre": nombre,
        "Descripcion": descripcion,
        "Precio": precio
    }

    productos.append(producto)
    print("Producto añadido")

#Método de baja, comprobamos que el codigo de producto existe, si existe, llamamos a la funcion
#que nos devuelve el indice de donde esta ese codigo en la lista,  preguntamos si está seguro de eliminar
#y si introduce s se borra, si introduce cualquier otra cosa no se borra
def bajaProducto():
    codigoProducto = input("Introduzca el codigo: ")
    if(comprobarExisteProducto(codigoProducto) == True):
        indice = devolverIndiceProducto(codigoProducto)
        print(productos[indice])
        decision = input("¿Seguro que desea eliminar? (s/n): ")
        if(decision == "s"):
            productos.pop(indice)
            print("producto eliminado")
        else:
            if(decision == "n"):
                print("producto no eliminado")
            else:
                print("opción incorrecta, no se ha eliminado nada")
    else:
        print("Este código de producto no existe")

#Método de modificacion, comprobamos que existe el producto, si existe
#llamamos a la funcion que nos devuelve donde esta ese producto en la lista
#pedimos los datos con la funcion auxiliar creada y le hacemos un pop, para eliminar
#primero, y luego lo insertamos en esa posicion
def modificacionProducto():
    codigoProducto = input("Introduzca el codigo: ")
    if (comprobarExisteProducto(codigoProducto) == True):
        indice = devolverIndiceProducto(codigoProducto)
        print(productos[indice])

        nombre, descripcion, precio = pedirDatos()

        producto = {
            "codArticulo": codigoProducto,
            "Nombre": nombre,
            "Descripcion": descripcion,
            "Precio": precio
        }
        productos.pop(indice)
        productos.insert(indice, producto)
        print("Producto modificado")
    else:
        print("Este código de producto no existe")

#Método de consulta, pedimos un codigo de producto, si existe,
#llamamos a la funcion que nos devuelve la posicion donde esta ese producto en la lista
#y lo mostramos, tambien puede buscar, por nombre y por precio, en estos casos se les mostrara todos los
#productos que contengan ese nombre o precio
def consultaProducto():
    print("1. Busqueda por codigo producto")
    print("2. Busqueda por nombre")
    print("3. Busqueda por precio")
    opcion = input("Introduzca opcion: ")
    if (opcion == "1"):
        codigoProducto = input("Introduzca el codigo: ")
        if (comprobarExisteProducto(codigoProducto) == True):
            print(productos[devolverIndiceProducto(codigoProducto)])
        else:
            print("Producto no encontrado")
    else:
        if (opcion == "2"):
            nombreProducto = input("Introduzca el nombre: ")
            if (comprobarExisteNombreProducto(nombreProducto) == True):
                mostrarNombreProductos(nombreProducto)
            else:
                print("Producto no encontrado")
        else:
            if (opcion == "3"):
                precioProducto = input("Introduzca el precio: ")
                if (comprobarExistePrecioProducto(precioProducto) == True):
                    mostrarPrecioProductos(precioProducto)
                else:
                    print("Producto no encontrado")
            else:
                print("opcion incorrecta")
while True:
    print("1. Alta producto")
    print("2. Baja producto")
    print("3. Modificación producto")
    print("4. Busqueda producto")
    print("5. Listado de productos")
    print("6. Salir")
    opcion = input("Introduzca la opcion deseada: ")

    if(opcion == "1"):
        altaProducto()
    else:
        if(opcion == "2"):
            bajaProducto()
        else:
            if(opcion == "3"):
                modificacionProducto()
            else:
                if(opcion == "4"):
                    consultaProducto()
                else:
                    if(opcion == "5"):
                        #Mostramos la lista
                        print(productos)
                    else:
                        if(opcion == "6"):
                            #Si pulsa el 6 se sale
                            print("Adios!")
                            break
                        else:
                            #si pulsa una opcion de las de fuera del rango, error
                            if (opcion < "1") or (opcion > "6"):
                                print("Opcion incorrecta, introduzca de nuevo")
