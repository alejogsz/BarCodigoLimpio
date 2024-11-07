from abc import ABC, abstractmethod



class IPedido(ABC):
    @abstractmethod
    def agregar_producto(self, producto, cantidad)->None:
        pass

    @abstractmethod
    def calcular_total(self)->None:
        pass