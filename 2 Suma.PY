  #  2 Inverso de número de tres cifras

        Numero3=int(input("Escribe un numero de 3 cifras : "))

        # Sacamos centenas, decenas y unidades
        centenas = int(Numero3 // 100)
        decenas = int(Numero3 // 10) % 10
        unidades = int(Numero3 % 10)

        # Mostramos el número invertido
        numero_invertido = unidades * 100 + decenas * 10 + centenas
        print("Numero : " , numero_invertido)
