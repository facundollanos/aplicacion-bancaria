from app.domain.clientes import Cliente


def registrar_cliente(nombre: str, apellido: str) -> Cliente:
    cliente = Cliente(
        nombre=nombre,
        apellido=apellido,
    )

    return cliente
