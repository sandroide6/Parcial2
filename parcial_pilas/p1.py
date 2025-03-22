class banco:
    def __init__(self, identificacion, tipocredito, valor):
        self.identificacion = identificacion
        self.tipocredito = tipocredito
        self.valor = valor
        

    def __init__(self):
        self.pila_creditos = []  # Pila principal

    def registrar_credito(self, identificacion, tipocredito, valor):
        pila_aux = []
        encontrada = False
        credi = None
        while self.pila_creditos:
            credi = self.pila_creditos.pop()
            if credi.identificacion == identificacion and credi.tipocredito == tipocredito:
                credi.valor += valor
                encontrada = True
            pila_aux.append(credi)

        while pila_aux:
            self.pila_creditos.append(pila_aux.pop())

        if not encontrada:
            self.pila_creditos.append(banco(identificacion, tipocredito,valor))
            print("Nuevo credito registrado.")
        else:
            print("Credito actualizado.")

    def actualizar_credito(self, identificacion, tipocredito):
        pila_aux = []
        encontrada = None
        actualizado=None
        while self.pila_creditos:
            credito = self.pila_creditos.pop()
            if credito.identificacion == identificacion and credito.tipocredito == tipocredito:
                encontrada = credito
                print("ingrese los nuevos datos")
                identificacionaux = input("Ingrese identificacion: ")
                tipocreditoaux = input("Ingrese tipocredito: ")
                valoraux = float(input("Precio: "))
                cantidadaux = int(input("Cantidad: "))
                actualizado=banco(identificacionaux, tipocreditoaux, valoraux, cantidadaux)
                
            pila_aux.append(actualizado)

        while pila_aux:
            self.pila_creditos.append(pila_aux.pop())

        if encontrada:
            print(encontrada)
        else:
            print("Usuario no encontrado.")

    def Adquirir_credito(self, identificacion, tipocredito, cantidad_vender):
        pila_aux = []
        vendido = False

        while self.pila_creditos:
            credito = self.pila_creditos.pop()
            if credito.identificacion == identificacion and credito.tipocredito == tipocredito:
                if cantidad_vender >= 0:
                    credito.valor += cantidad_vender
                    print(f"Venta de credito exitosa. Valor Actualizado: {credito.valor}")
                    vendido = True
                    if credito.cantidad > 0:
                        pila_aux.append(credito)
                else:
                    print("El valor de la venta no puede ser cero o negativo.")
                    pila_aux.append(credito)
            else:
                pila_aux.append(credito)

        while pila_aux:
            self.pila_creditos.append(pila_aux.pop())

        if not vendido:
            print("El usurio no esta registrado en el banco.")



    def Eliminar_credito(self, identificacion, tipocredito):
        pila_aux = []
        vendido = False

        while self.pila_creditos:
            prenda = self.pila_creditos.pop()
            if prenda.identificacion == identificacion and prenda.tipocredito == tipocredito:
                    prenda = prenda.pop()
                    print("Credito eliminado")
                    vendido = True
                    pila_aux.append(prenda)

        while pila_aux:
            self.pila_creditos.append(pila_aux.pop())

        if not vendido:
            print("El usurio no esta registrado en el banco.")


    def consultar_creditos(self):
        pila_aux = []
        if not self.pila_prendas:
            print("No hay creditos disponibles.")
            return

        print("Creditos disponibles:")
        while self.pila_prendas:
            creditos = self.pila_prendas.pop()
            print(creditos)
            pila_aux.append(creditos)

        while pila_aux:
            self.pila_prendas.append(pila_aux.pop())