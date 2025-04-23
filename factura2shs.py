Nproducto = []
Preciounitario= []
precioFinal=0
descuento=0
pfdescuento=0
while True:
    try:
        CantidadProductos = int(input("Ingrese la cantidad de productos: "))
        if CantidadProductos > 0:
            break  # Si el número es mayor a 0, sale del ciclo
        else:
            print("ERROR: La cantidad debe ser mayor a 0. Intenta de nuevo.")
    except ValueError:
        print("ERROR: Debes ingresar un número válido. Intenta de nuevo.")

for i in range(CantidadProductos):
    Nproducto.append(input("Ingrese nombre del producto: "))
    Preciounitario.append(int(input("Ingrese el precio del producto: ")))
    precioFinal = precioFinal + Preciounitario[i]



for i in range(CantidadProductos):
      print(f"{Nproducto[i]} {Preciounitario[i]}")


print(f"El precio total de sus productos comprados es {precioFinal}")

if CantidadProductos >= 3:  
        descuento = precioFinal * (30/100)
        pfdescuento = precioFinal - descuento
        print(f"El descuento es del 30% y su valor a pagar es {pfdescuento}")



# for i in range(1,CantidadProductos):
#     print(Nproducto[CantidadProductos])
#     print(Preciounitario[CantidadProductos])


    






# Preciounitario=int(input("ingrese el precio del producto: 

# porcentajedescuento=float(0.30)