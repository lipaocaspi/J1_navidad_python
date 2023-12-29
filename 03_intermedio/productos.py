productos = []
registroProducto = []
indice = -1
isIncorrect = True

def regProducto(valorDato, nombreDato, tipoDato):
    global isIncorrect
    isIncorrect = True
    valorDato = 0
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"Ingrese {nombreDato} del producto: "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            if (nombreDato == "código (3 cifras)" and len(str(valorDato)) != 3):
                regProducto(valorDato, nombreDato, tipoDato)
            else :
                registroProducto.append(valorDato)
                isIncorrect = False
    return valorDato

def mostrarInventario():
    print(f"INVENTARIO")
    print(f"------------------------------------------------------------------------------------------------------------------------")
    print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("CÓDIGO", "NOMBRE", "VALOR COMPRA", "VALOR VENTA", "STOCK MÍNIMO", "STOCK MÁXIMO", "STOCK ACTUAL", "NOMBRE PROVEEDOR"))
    for i in range(len(productos)):
        print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(productos[i][0], productos[i][1], productos[i][2], productos[i][3], productos[i][4], productos[i][5], productos[i][6], productos[i][7]))
    print(f"")

def buscarProducto(codigoProducto : int) -> int:
    global indice
    indice = -1
    for item in productos:
        if codigoProducto in item:
            indice = productos.index(item)
    if (indice == -1):
        print(f"No se encontró el producto")
    return indice

def actStock():
    isIncorrect = True
    while (isIncorrect):
        if (indice < 0):
            isIncorrect = False
        else:
            try:
                stock = int(input(f"Ingrese el valor del stock que desee agregar o restar (ingrese un número negativo en ese caso) : "))
            except ValueError:
                print(f"Ingrese un dato válido")
            else:
                if (stock < 0 and abs(stock) > productos[indice][6]):
                    print(f"No es posible realizar esta actualización, el valor del stock no puede ser menor a 0")
                else:
                    productos[indice][6] = int(productos[indice][6]) + stock
                    isIncorrect = False

def imprimirInforme():
    print(f"INFORME DE PRODUCTOS CRÍTICOS")
    print(f"------------------------------------------------------------------------------------------------------------------------")
    print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("CÓDIGO", "NOMBRE", "VALOR COMPRA", "VALOR VENTA", "STOCK MÍNIMO", "STOCK MÁXIMO", "STOCK ACTUAL", "NOMBRE PROVEEDOR"))
    for i in range(len(productos)):
        if (productos[i][6] < productos[i][4]):
            print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(productos[i][0], productos[i][1], productos[i][2], productos[i][3], productos[i][4], productos[i][5], productos[i][6], productos[i][7]))
    print(f"")

def calGanaciaP() -> int:
    suma = 0
    for i in range(len(productos)):
        suma = suma + (int(productos[i][3]) - int(productos[i][2])) * int(productos[i][6])
    print(f"GANANCIA POTENCIAL : ${suma}")
    return suma