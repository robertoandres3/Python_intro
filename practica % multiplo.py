
numero= int(input(" Escribe tu Numero "))

if (numero % 3 == 0) and (numero % 5 == 0):
    print("Buzzfizz")
elif (numero % 5 == 0):
    print("buzz")

elif (numero % 3 == 0):
    print("fizz")

else:
    print(numero)


