from Usuario import Usuario
from Pedido import Pedido
from GestionPedido import GestionPedidos
from Producto import Producto

class Mesero(Usuario):
    def __init__(self, nombre: str, contraseña: str):
        super().__init__(nombre, contraseña)
        self.pedidos_atendidos: list[Pedido] = []  # Lista de pedidos atendidos por el mesero
        self.propinas: int = 0  # Propinas acumuladas
        self.gestion_pedidos = GestionPedidos()  # Creamos el objeto GestionPedidos dentro de la clase

    def registrar_pedido(self, pedido_id: int, productos: list[Producto], total: float) -> None:
        # Llama a GestionPedidos para registrar un nuevo pedido
        self.gestion_pedidos.registrar_pedido(pedido_id, productos, total)
        nuevo_pedido = self.gestion_pedidos.pedidos[pedido_id]
        self.pedidos_atendidos.append(nuevo_pedido)
        print(f"Pedido {pedido_id} registrado y asignado al mesero {self.nombre}.")

    def ver_pedido(self, pedido_id: int) -> None:
        # Llama a GestionPedidos para ver el detalle de un pedido específico
        pedido = self.gestion_pedidos.ver_pedido(pedido_id)
        if pedido:
            print(f"Detalles del pedido {pedido_id}: {pedido}")

    def liquidar_factura(self, pedido_id: int) -> None:
        # Llama a GestionPedidos para liquidar la factura de un pedido
        self.gestion_pedidos.liquidar_factura(pedido_id)
        # Después de liquidar la factura, el mesero puede recibir propinas (simularemos una lógica simple)
        self.propinas += 5  # Propina fija de ejemplo
        print(f"Factura del pedido {pedido_id} liquidada. Propinas acumuladas: ${self.propinas}")
