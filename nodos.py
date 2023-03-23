class nodo():
    def __init__(self, data):
        self.anterior = None
        self.posterior = None
        self.data = data

class DLE(object):
    def __init__(self):
        self.primero = None
        self.next = None
        self.cantidad = 0

    def vacio(self):
        return self.next == None
    
    def insertar(self,data):
        ctm = nodo(data)
        if self.vacio():
            self.next = self.primero = ctm
        else:
            gary = self.primero
            self.primero = gary.posterior = ctm
            self.primero.anterior = gary
        self.cantidad +=1

    def leer(self):
        LeerNodo = self.next
        while LeerNodo:
            print(LeerNodo.data)
            LeerNodo = LeerNodo.posterior

    def MatrixCalORG(self, indice):
        if self.vacio():
            return None
        if indice >= self.cantidad:
            print("Penalizado")
            return None
        contador = 0
        ElementoPivote = self.next
        while ElementoPivote != None:
            if contador == indice:
                return ElementoPivote.data
            ElementoPivote = ElementoPivote.posterior
            contador +=1
        return None