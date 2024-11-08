from typing import Dict
from Producto import Producto

class Pedido:
    cont=1
    def __init__(self, estado: str = "pendiente"):
        self.cont+=1
        self.pedido_id = self.cont
        self.estado = estado  
        self.productos: Dict[Producto, int] = {} 

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
        print(f"{cantidad} unidades de {producto.nombre} agregadas al pedido {self.pedido_id}.")

    def calcular_total(self) -> float:
        total = sum(producto.obtener_precio() * cantidad for producto, cantidad in self.productos.items())
        print(f"Total del pedido {self.pedido_id}: ${total:.2f}")
        return total

    def __str__(self) -> str:
        detalles_productos = ", ".join(f"{producto.nombre} x{cantidad}" for producto, cantidad in self.productos.items())
        return f"Pedido {self.pedido_id} [{self.estado}]: {detalles_productos} - Total: ${self.calcular_total():.2f}"

