#  3 Extraer hora, minuto y segundo de segundos totales

                numersegundo= int(input("Escribe los segundos en numeros sin puntos ni comas : "))

                # 1 hora = 60 minuutos y 3600 segundos 
                # 1 minut = 60 segund

                horas = numersegundo // 3600
                segundos_restantes = numersegundo % 3600
                minutos = segundos_restantes // 60

                # Segundos que sobran después de sacar los minutos
                segundos = segundos_restantes % 60

                print (f"{horas} hora(s), {minutos} minuto(s), {segundos} segundo(s).")
