
inventario= {}


def añadir():
    nombre= input("Escribe el nombre del producto: ").lower()
    precio= int(input("Escribe el precio del producto: "))
    cantidadispo= int(input("Escribe la cantida de productos: "))
    inventario[nombre]= {"precio": precio ,"cantidadispo": cantidadispo}
    print("Tu información a sido guardada")
    print(f"tu producto es {nombre} y su precio es {precio} con la cantidad {cantidadispo} ")

def consultar():
    while True:

        nombrebusca= input("Escribe el nombre del producto que deseas buscar: ").lower()
        if nombrebusca in inventario:
            print (f"nombre:", nombrebusca  )
            print ("precio:", inventario[nombrebusca]["precio"])
            print ("cantidad:", inventario[nombrebusca]["cantidadispo"])
            break
        else:
            print("No existe el producto")

def actualizar():       
    while True:

        nombredelproduc=input("Escribe el nombre del producto que desea modificar el precio: ").lower()
        if nombredelproduc in inventario:
            inventario[nombredelproduc]["precio"]=int(input("Escribe tu nuevo precio"))
            print("Modificaste tu precio")

            break
        else:
            print("Este producto no existe")

def eliminar():
     nombreelim= input("Escribe el nombre que deseas eliminar: ").lower()
     if nombreelim in inventario:
         del inventario [nombreelim] 
     print("Tus datos fueron eliminados ")    

def calculavalototal():
    total = 0
    general = 0
    for clave,datos in inventario.items():
        total += datos['precio'] * datos['cantidadispo']
        print (f"la suma total de {clave} es: {total}")
        general = general + total

    print(general)
        


def mostrartodo():
     print ("Estos son todos los productos")
     for x,y in inventario.items():
        print (f" Producto: {x}")
        print (f" precio: {y["precio"]}")
        print (f" Cantidad disponible: {y["cantidadispo"]}")




while True:
    try:
            print("\n\033[33m\033[1mMENÚ\n")

            print("\033[0mEscoja una de las Opciones:\n" 
                \
            "1. Añadir productos\n" \
            "2. Consultar productos\n" \
            "3. Actualizar precios\n" \
            "4. Eliminar productos\n" \
            "5. Calcular el valor total del inventario\n" \
            "6. Mostrar todos los productos con su información")

            opcion=int(input("\nEscribe una opción: "))

            match opcion:
                case 1:
                    añadir()
                case 2:
                    consultar()
                case 3:
                    actualizar()
                case 4:
                    eliminar()

                case 5:
                    calculavalototal()

                case 6:
                    mostrartodo()
                      

                case _:
                    
                    print("Elige una opcion correcta")
    except ValueError:
            print("Escriba un numero correcto")
