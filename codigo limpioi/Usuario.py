from GestionPedido import GestionPedido
from GestionMesas import GestionDeMesas
from abc import ABC

class Usuario(ABC):
    def __init__(self, nombre: str)->None:
        self.nombre:str = nombre

    
    def ver_mesas(self, gestion_mesas:GestionDeMesas)->None:
        gestion_mesas.visualizar_mesas

   
    def ver_pedidos(self, gestion_pedidos:GestionPedido)->None:
        gestion_pedidos.visualizar_pedido
