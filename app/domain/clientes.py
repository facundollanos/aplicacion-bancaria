from dataclasses import dataclass, field
from datetime import datetime,timezone
from uuid import UUID,uuid4

@dataclass
class Cliente:
    nombre:str
    apellido:str
    id: UUID = field(default_factory=uuid4)
    fecha_alta: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    