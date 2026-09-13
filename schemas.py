from pydantic import BaseModel
from typing import List, Union


class HistoriaRequest(BaseModel):
    id_partida: Union[int, str]
    nodo_actual: str
    decision_usuario: str
    inventario: List[str]