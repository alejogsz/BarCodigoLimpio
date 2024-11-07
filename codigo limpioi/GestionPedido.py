from Pedido import Pedido
from typing import Optional


class GestionPedidos:
    def __init__(self):
        self.pedidos: dict[int, Pedido] = {}  # Diccionario de pedidos con ID de pedido como clave

    def registrar_pedido(self, pedido_id: int, productos: list[str], total: float) -> None:
        nuevo_pedido = Pedido(pedido_id, productos, total)
        self.pedidos[pedido_id] = nuevo_pedido
        print(f"Pedido {pedido_id} registrado con éxito.")

    def ver_pedido(self, pedido_id: int) -> Optional[Pedido]:
        if pedido_id in self.pedidos:
            pedido = self.pedidos[pedido_id]
            print(f"Pedido {pedido_id}: {pedido.productos} - Total: ${pedido.total}")
            return pedido
        else:
            print("Pedido no encontrado.")
            return None

    def liquidar_factura(self, pedido_id: int) -> None:
        if pedido_id in self.pedidos:
            del self.pedidos[pedido_id]
            print(f"Factura del pedido {pedido_id} liquidada con éxito.")
        else:
            print("Pedido no encontrado.")