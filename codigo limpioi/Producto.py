

class Producto:
    def __init__(self, nombre:str , precio:int)->None:
        self.nombre:str = nombre
        self.precio:int = precio

    def obtener_precio(self)->int:
        return self.precio