from Pedido import Pedido
from abc import ABC, abstractmethod

class IMesa(ABC):
    @abstractmethod
    def agregar_pedido(self, pedido:Pedido)->None:
        pass

    @abstractmethod
    def calcular_total(self)->None:
        pass

    @abstractmethod
    def cambiar_estado(self, estado:str)->None:
        pass