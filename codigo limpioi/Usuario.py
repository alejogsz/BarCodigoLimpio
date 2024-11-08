from GestionPedido import GestionPedido
from GestionMesas import GestionDeMesas
from typing import Optional

class Usuario:
    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self.contraseña = contraseña

    def registrar_pedido(self, pedido_id: int) -> None:
        # Este método llamará a la funcionalidad de GestionPedidos para registrar el pedido
        print(f"{self.nombre} ha registrado un pedido con ID: {pedido_id}")
        

