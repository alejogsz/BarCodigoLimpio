from Producto import Producto
from Mesa import Mesa
from Mesero import Mesero
from Administrador import Administrador
from GestionMesas import GestionDeMesas
from GestionPedido import GestionPedido


def main():
    cerveza = Producto("Cerveza", 3.0)
    pizza = Producto("Pizza", 8.0)

    gestion_mesas = GestionDeMesas()

    mesa1 = Mesa(1)
    mesa2 = Mesa(2)
    mesa3 = Mesa(3)

    gestion_mesas.agregar_mesa(mesa1)
    gestion_mesas.agregar_mesa(mesa2)
    gestion_mesas.agregar_mesa(mesa3)

    mesero1 = Mesero("Carlos")
    mesero2 = Mesero("Ana")

    mesero1.mesas_asignadas.append(mesa1)
    mesero2.mesas_asignadas.append(mesa2)

    admin = Administrador("Luis")

    print("\nMesero Carlos realiza su trabajo:")
    gestion_pedidos = GestionPedido()
    pedido1 = gestion_pedidos.crear_pedido()
    pedido1.agregar_producto(cerveza, 2)
    pedido1.agregar_producto(pizza, 1)
    mesero1.registrar_pedido(mesa1, pedido1)
    mesero1.liquidar_factura(pedido1, 10)
    mesero1.ver_mesas(gestion_mesas)

    print("\nAdministrador Luis realiza su trabajo:")
    admin.ver_mesas(gestion_mesas)
    admin.ver_propinas_meseros([mesero1, mesero2])

if __name__ == "__main__":
    main()