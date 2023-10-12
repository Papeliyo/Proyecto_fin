from datetime import date
from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    id: Optional[int]
    titulo: str
    descripcion: str
    fecha_vencimiento: date
