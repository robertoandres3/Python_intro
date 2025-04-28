# Ejercicios Python 1.1 

# 1 Intercambio de variables

# Numero1= int(input("Ingresa un numero sin comas ni puntos :"))
# Numero2= int(input("Ingresa un segundo numero sin comas ni puntos :"))
# print("numeros ingresados" )
# print("A = " , Numero2  ) 
# print("B = " , Numero1)

      


              


        # 4 Fecha formateada

        dia = input("Introduce el día: ")
        mes = input("Introduce el mes: ")
        año = input("Introduce el año: ")

        print(f"{dia}/{mes}/{año}")
        print(f"{año}-{mes}-{dia}")

        # 5. Convertir temperatura (F ↔ C)

        
        f = float(input("Introduce la temperatura en Fahrenheit: "))
        celsius = (f - 32) * 5 / 9

        print(f"{f}°F son {celsius:.2f}°C")

        # 6  Cálculo de propina y cuenta total

        pagocomida= int(input("ingresa el costo de tu comida: "))

        propina_10 = pagocomida  * 0.10
        propina_15 = pagocomida * 0.15
        propina_20 = pagocomida  * 0.20

        total_10 = pagocomida + propina_10
        total_15 = pagocomida + propina_15
        total_20 = pagocomida + propina_20


        print(f"\nCon 10% de propina: ${total_10}")
        print(f"Con 15% de propina: ${total_15}")
        print(f"Con 20% de propina: ${total_20}")


        # print(f"\nCon 10% de propina: ${total_10:.2f}")
        # print(f"Con 15% de propina: ${total_15:.2f}")
        # print(f"Con 20% de propina: ${total_20:.2f}")
