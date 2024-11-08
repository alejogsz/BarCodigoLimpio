from Mesero import Mesero


class GestionMeseros:
    def __init__(self):
        self.meseros: list[Mesero] = []  # Lista de meseros

    def agregar_mesero(self, nombre: str, contraseña: str) -> None:
        # Crear un nuevo mesero y añadirlo a la lista
        nuevo_mesero = Mesero(nombre, contraseña)
        self.meseros.append(nuevo_mesero)
        print(f"Mesero {nombre} agregado al sistema.")

    def ver_numero_atendidos(self, mesero_id: str) -> int:
        # Busca al mesero por su nombre y retorna la cantidad de pedidos atendidos
        for mesero in self.meseros:
            if mesero.nombre == mesero_id:
                return len(mesero.pedidos_atendidos)
        print("Mesero no encontrado.")
        return 0

    def ver_propinas_mesero(self, mesero_id: str) -> int:
        # Busca al mesero por su nombre y retorna el total de propinas
        for mesero in self.meseros:
            if mesero.nombre == mesero_id:
                return mesero.propinas
        print("Mesero no encontrado.")
        return 0
