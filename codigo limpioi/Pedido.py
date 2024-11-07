from IPedido import IPedido
from Producto import Producto


class Pedido(IPedido):
    def __init__(self)->None:
        self.productos:dict[Producto,int]= {}
        self.estado:str = 'Pendiente'

    def agregar_producto(self, producto:Producto, cantidad:int)->None:
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def calcular_total(self)->int:
        total = 0
        for producto, cantidad in self.productos.items():
            total += producto.obtener_precio() * cantidad
        return total
