from Usuario import Usuario
from GestionMesas import GestionMesas
from GestionPedido import GestionPedidos
from gestionmesero import GestionMeseros
 
class Administrador(Usuario):
    def __init__(self, nombre: str, contraseña: str):
        super().__init__(nombre, contraseña)
        self.gestion_mesas = GestionMesas()
        self.gestion_meseros = GestionMeseros()
        self.gestion_pedidos = GestionPedidos()

    def ver_mesas(self) -> None:
        # Llama a GestionMesas para obtener el estado de las mesas
        mesas_estado = self.gestion_mesas.ver_mesas()
        for estado in mesas_estado:
            print(estado)

    def ver_gastos_mesas(self) -> None:
        # Llama a GestionMesas para obtener los gastos de las mesas
        gastos = self.gestion_mesas.ver_gastos_mesas()
        for mesa_numero, gasto in gastos.items():
            print(f"Mesa {mesa_numero}: Gasto ${gasto:.2f}")

    def ver_numero_atendidos(self, mesero_id: str) -> None:
        # Llama a GestionMeseros para ver la cantidad de pedidos atendidos por un mesero específico
        cantidad_atendidos = self.gestion_meseros.ver_numero_atendidos(mesero_id)
        print(f"El mesero {mesero_id} ha atendido {cantidad_atendidos} pedidos.")

    def ver_propinas_mesero(self, mesero_id: str) -> None:
        # Llama a GestionMeseros para ver el total de propinas de un mesero específico
        propinas = self.gestion_meseros.ver_propinas_mesero(mesero_id)
        print(f"El mesero {mesero_id} ha recibido ${propinas} en propinas.")
