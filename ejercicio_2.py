cantidad_sala = 30

while True:
    print("=== Menú ===")
    print("1. Salas disponibles")
    print("2. Reservar salas")
    print("3. Liberar salas")
    print("4. Historial")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("ingrese una opción: "))
            break
        except: 
            print("debe ingresar una opción valida")

    if opcion == 1:
        print("La cantidad de salas disponibles es: ", cantidad_sala)

    elif opcion == 2:
        while True:
            try:
                reserva = int(input("Ingrese la cantidad de las salas a reserva: "))
                restante = cantidad_sala - reserva
                print("La cantidad restante es: ", restante)
                if reserva <= 0:
                    
                    print("la cantidad debe ser un numero entero positivo")
                else:
                    if reserva > cantidad_sala:
                        print("La cantidad de reservas, no puede superar al total de salas disponibles") 
                    else: 
                        break
            except:
                print("La cantidad debe ser un numero entero positivo")


    elif opcion == 3:
        while True:
             
    elif opcion == 4:
        print("opción 4")
    elif opcion == 5:
        print("Gracias por tu visita")
        break
    else:
        print("Opción invalida")

         
 