from pydantic import BaseModel, Field

class ClienteCrear(BaseModel):
    nombre: str = Field(min_length=1,max_length=100)
    apellido: str = Field(min_length=1, max_length=100)
