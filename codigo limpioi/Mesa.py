from Pedido import Pedido

class Mesa:
    def __init__(self, numero: int):
        self.numero = numero
        self.estado = "libre"
        self.gasto = 0.0  # Gasto acumulado en la mesa

    def cambiar_estado(self, nuevo_estado: str) -> None:
        self.estado = nuevo_estado