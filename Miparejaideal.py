
# Vamos a dividirlo en 3 areas:

# FISICO / MENTAL / ESPIRITUAL 

# Fisico= Sexo definido, Aseo, ejercicio, fiestas, hacer el amor, situacion economica
# Mental = Proyectos, estudios, habitos de desarrollo, fidelidad y perspectiva de pareja 
# Espiritual = creencias, situacion sentimental, situacion familiar,  habitos. 

print ("Cuestionario de pareja Ideal")
puntaje= 0
nombre= input("¿Cual es tu nombre? : ")
Edad=int(input("Cual es tu Edad : "))


# PREGUNTAS FISICO

if Edad >= 18:
    Preguntaf1=input("¿Eres 100% mujer? : ").lower()

    if Preguntaf1 == "si":
        puntaje=puntaje + 10
        print(puntaje)

        #2 aseo 

        preguntaf2=input("¿te gusta bañarte? : ").lower()

        if preguntaf2 == "si":
            puntaje = puntaje +10

        else:
            preguntaf2 == "no" 
            puntaje == puntaje -10
            print ("estas bien cochina")
        print(puntaje)

        preguntaf3=input(" ¿Te gusta hacer ejercicio ?(Responde si, no o talvez) :")
        print(puntaje)

        #3 ejercicio

        if preguntaf3 == "si":
            puntaje = puntaje +10 

        elif preguntaf3 == "talvez":
            puntaje =puntaje +5

        elif preguntaf3 == "no":
            puntaje = puntaje -5
        print(puntaje)

        # 4 Fiesta

        preguntaf4= input("¿Te gusta la fiesta ? (Responde si, no, a veces) :")
        

        if preguntaf4 == "si":
            puntaje = puntaje -5

        elif preguntaf4 == "a veces":
            puntaje = puntaje +5

        elif preguntaf4 == "no":
            puntaje = puntaje + 10
        
    
        print ("tu puntaje total es " , puntaje) 

        if puntaje >= 30:
                print("casemonos")
        
        else:
            print(" vete al carajo")




    else:
        Preguntaf1 == "no"
        print("No eres ideal para mi")
 
else:
    print("Eres menor edad, ponte a estudiar")








