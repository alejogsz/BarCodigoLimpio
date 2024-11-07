from Mesa import Mesa

class GestionDeMesas:
    def __init__(self)->None:
        self.mesas:list[Mesa] = []

    def agregar_mesa(self, mesa:Mesa)->None:
        self.mesas.append(mesa)

    def visualizar_mesas(self)->str:
        for mesa in self.mesas:
            print(f"Mesa {mesa.id} - Estado: {mesa.estado} - Total: {mesa.calcular_total()}")
