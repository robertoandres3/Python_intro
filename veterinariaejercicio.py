

print ("Hola bienvenido a nuestro veterinaria\n")


nombre =[]
edad = []
enfermo = []

def  opcion1():

    nombremascota = input("Como se llama tu mascota ?: ").lower()
    nombre.append(nombremascota)
    edadmascota = input("Cuantos años tiene ? : ")
    edad.append(edadmascota)
    enfermomascota =(input("Esta enfermo ? : (escribe si/no) "))
    enfermo.append(enfermomascota)

def opcion2():
     
    animalelim= input("Ingresa nombre de mascota a eliminar: ").lower()
    if animalelim in nombre:

        indice = nombre.index(animalelim)
                    
        del nombre[indice]
        del edad[indice]
        del enfermo [indice]
        print("haz eliminado a ", animalelim)
    else:
                     print ("No existe el nombre de la mascota")


def opcion3():
      
    print ("Estos son todos datos registrados?\n")
    for i in range(len(nombre)):
        print(f"{nombre[i]} {edad[i]} años {enfermo[i]} esta enfermo")
        


while True: 
    print (" MENÚ\n"
        
    "1. Agregar un nombre de tu animal\n" \

    "2. Eliminar animal\n" \

    "3. lista de animales registrados\n" \
    "4. salir\n") 

    opcion= int(input("Ingresa un numero: "))

    match opcion:
            case 1: 
                opcion1()
                

            case 2: 
                opcion2()



            case 3: 
                opcion3()
               
        
            case 4:
                print("Saliendo del programa...")
                break
                

