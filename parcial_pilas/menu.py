from p1 import banco

def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar Credito")
    print("2. Actualizar Credito")
    print("3. Adquirir credito")
    print("4. Eliminar credito")
    print("4. Consultar creditos")
    print("5. Salir")



while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        identificacion = input("identificacion: ")
        tipocredito = input("tipocredito: ")
        valor = int(input("valor: "))
        banco.registrar_credito(identificacion,tipocredito,valor)

    elif opcion == "2":
        identificacion = input("Ingrese identificacion: ")
        tipocredito = input("Ingrese tipocredito: ")
        banco.actualizar_credito(identificacion, tipocredito)

    elif opcion == "3":
        identificacion = input("identificacion: ")
        tipocredito = input("tipocredito: ")
        cantidad = int(input("Cantidad a vender: "))
        banco.Adquirir_credito(identificacion, tipocredito, cantidad)
        
    elif opcion == "4":
        identificacion = input("identificacion: ")
        tipocredito = input("tipocredito: ")
        banco.Eliminar_credito(identificacion, tipocredito)


    elif opcion == "5":
        banco.consultar_creditos()

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")