from typing import List, Dict
from Mesa import Mesa

class GestionMesas:
    def __init__(self):
        self.mesas: Dict[int, Mesa] = {}  # Diccionario de mesas con número de mesa como clave

    def agregar_mesa(self, numero: int) -> None:
        if numero not in self.mesas:
            self.mesas[numero] = Mesa(numero)
        print(f"Mesa {numero} agregada al sistema.")

    def ver_mesas(self) -> List[str]:
        return [f"Mesa {numero}: {mesa.estado}" for numero, mesa in self.mesas.items()]

    def ver_gastos_mesas(self) -> Dict[int, float]:
        return {numero: mesa.gasto for numero, mesa in self.mesas.items()}

