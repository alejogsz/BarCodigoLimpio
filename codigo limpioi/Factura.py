from Pedido import Pedido

class Factura:
    def __init__(self, pedido:Pedido, propina:int)->None:
        self.pedido:Pedido = pedido
        self.propina:int = 5

    def calcular_total(self)->int:
        return self.pedido.calcular_total() + self.calcular_propina()

    def calcular_propina(self)->int:
        return self.pedido.calcular_total() * (self.propina / 100)

    def liquidar(self)->None:
        self.pedido.estado = 'Facturado'
