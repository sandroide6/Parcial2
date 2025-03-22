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






identificacion = input("identificacion: ")
tipocredito = input("tipocredito: ")
valor = int(input("valor: "))
banco(identificacion,tipocredito,valor)
registrar_credito()