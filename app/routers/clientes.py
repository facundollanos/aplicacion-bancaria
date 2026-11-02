from fastapi import APIRouter
from app.schemas.clientes import ClienteCrear
from app.services.clientes import registrar_cliente

router = APIRouter(
    prefix = "/clientes",
    tags = ["Clientes"],
)

@router.get("/")
def listar_clientes():
    return []

@router.post("/", status_code=201)
def crear_cliente(datos:ClienteCrear):
    cliente = registrar_cliente(nombre= datos.nombre,
                                apellido=datos.apellido)
    return cliente