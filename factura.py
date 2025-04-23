# nombre=print(input("Bienvenido, Escriba Nombre de Usuario "))

# celular= int(input(" Numero de Celular"))

# cedula= int(input(" Numero de Cedula " )) 

# corre= input(" Correo Electronico " ) 

# edad= int(input("Edas cliente "))


Canprodu= int(input( " ¿Cuantos Productos vas a Comprar? ") )
              
Nproducto= input( "ingrese Nombre del producto : ") 

Precioprod=int(input(" Precio del Producto "))




PrecioFinal=int(Canprodu * Precioprod)

print(" Precio final es ", PrecioFinal) 

if Canprodu >= 3 and Canprodu < 7: 
    print("Tienes un Descuento del 30 porciento")

    Preciodescuento= PrecioFinal *(30/100)

elif Canprodu >= 7:
    print(" tienes un descuento del 50% ")

    Preciodescuento= PrecioFinal *(50/100)

else:
    print( "No tienes descuento")
    

PrecioFinal=PrecioFinal-Preciodescuento



print(" Tu Precio con descuento es " , PrecioFinal) 



